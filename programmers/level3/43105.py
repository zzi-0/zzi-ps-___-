def solution(triangle):
    answer = 0
    arr = sum(triangle, [])
    n = len(arr) + 1
    dp = [0 for _ in range(n)]
    index = 0

    
    for level in range(len(triangle)):
        for i in range(len(triangle[level])):
            index += 1
            if i == 0 or i == level:
                dp[index] = dp[level] + triangle[level][i]
            else:
                print("index - level + i",index - level + i)
                dp[index] = max(dp[index - level + i] + triangle[level][i], dp[index - level + i + 1] + triangle[level][i])
    
    print(dp)
    return answer



print(solution([[7], [3, 8], [8, 1, 0]]))