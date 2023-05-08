from itertools import permutations
import math

def solution(n, weak, dist):
    min_count = math.inf
    weak_len = len(weak)
    weak = weak + [w + n for w in weak]

    for start in range(weak_len):
        for friends in list(permutations(dist, len(dist))):
            # 몇 번 째 친구인지
            count = 1
            # 현재 위치의 인덱스
            pos = start
            for i in range(1, weak_len):
                next_pos = start + i
                diff = weak[next_pos] - weak[pos]
                if diff > friends[count-1]:
                    pos = next_pos
                    count += 1
                    if count > len(dist):
                        break
        
            if count <= len(dist):
                min_count = min(count, min_count)
    
    if min_count == math.inf:
        return -1
    else:
        return min_count
    

print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
print(solution(	12, [1, 3, 4, 9, 10], [3, 5, 7]))

""" 0 1 2 3 4 5 6 7 8 9 10 11
0,1,0,0,0,1,1,0,0,0, 1, 0 """

# dist 정렬 제일 큰 애부터 8
#  15, 간격 -1이면 가능!
