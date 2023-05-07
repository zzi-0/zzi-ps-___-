
def solution(scores):
    answer = 1
    target = scores[0]
    target_sum = sum(target)
    scores.sort(key=lambda x:(-x[0], x[1]))
    before = 0
    
    for score in scores:
        if score[0] > target[0] and score[1] > target[1]:
            return -1
        if before <= score[1]:
            if target_sum < sum(score):
                answer += 1
            before = score[1]


    return answer

print(solution([[3,2],[1,1],[7,2],[3,2],[5,1]]))