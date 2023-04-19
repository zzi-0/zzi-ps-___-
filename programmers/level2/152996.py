from collections import defaultdict

def solution(weights):
    answer = 0
    info = defaultdict(int)
    for w in weights:
        answer += info[w]
        answer += info[w*2]
        answer += info[w/2]
        answer += info[(w*2)/3]
        answer += info[(w*3)/2] 
        answer += info[(w*4)/3]
        answer += info[(w*3)/4]
        info[w] += 1
    return answer

print(solution([100,180,360,100,270]))