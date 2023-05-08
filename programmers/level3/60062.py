import time
from collections import deque

class LoopBreak(Exception):
    pass


def solution(n, weak, dist):
    answer = -1
    dist.sort(reverse=True)
    w_check = [0] * (n)
    d_check = [0] * len(dist)

    for w in weak:
        w_check[w] = 1

    queue = deque()
    queue.append((w_check,d_check))

    while len(queue):
        try:
            w_check,d_check = queue.popleft()
            for i in range(n):
                for j in range(len(dist)):
                    if w_check[i] == 1 and d_check[j] == 0:
                        w_check_copy = w_check[:]
                        d_check_copy = d_check[:]
                        for k in range(i,i+dist[j]+1):
                            w_check_copy[k%n-1] = 0
                        d_check_copy[j] = 1
                        if not 1 in w_check_copy:
                            answer = sum(d_check_copy)
                            raise LoopBreak()
                        queue.append((w_check_copy,d_check_copy))
        except LoopBreak:
            break
    return answer
    
start = time.time()
print(solution(	12, [1, 3, 4, 9, 10], [3, 5, 7]))
end = time.time()

print(end - start)


""" 0 1 2 3 4 5 6 7 8 9 10 11
0,1,0,0,0,1,1,0,0,0, 1, 0 """

# dist 정렬 제일 큰 애부터 8
#  15, 간격 -1이면 가능!
