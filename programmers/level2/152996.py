from itertools import combinations, product

def solution(weights):
    answer = 0
    weights.sort()
    for [c1, c2] in combinations(weights,2):
        for [p1, p2] in product([2,3,4], repeat=2):
            if c1*p1 == c2*p2:
                answer += 1
                break
    return answer

print(solution([100,180,360,100,270]))