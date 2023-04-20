def solution(n):
    dp = [0] * (n+1)
    dp[2] = 3
    
    for i in range(3,n+1):
        if i % 2 == 0:
            dp[i] += dp[i-2] * 3 + 2
            for j in range(i-4,0,-2):
                dp[i] += dp[j] * 2
    return dp[n] % 1000000007


print(solution(6))