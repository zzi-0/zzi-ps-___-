def solution(scores):
    answer = 1
    n = len(scores)
    out = [0] * n
    score = sum(scores[0])

    for i in range(n):
        [i_a, i_b] = scores[i]
        for j in range(i):
            [j_a, j_b] = scores[j]
            if i_a < j_a and i_b < j_b:
                out[i] = 1
                break
        for j in range(i+1,n):
            [j_a, j_b] = scores[j]
            if i_a < j_a and i_b < j_b:
                out[i] = 1
                break
        if i == 0: 
            if out[0] == 1:
                return -1
        else:
            if score < sum(scores[i]) and out[i] == 0:
                answer += 1

    
    return answer

print(solution([[2,2],[1,4],[3,2],[3,2],[1,1]]))