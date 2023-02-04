def solution(n, money):
    answer = 0
    dp = [1] + [0] * n
    for m in money:
        for i in range(m,n+1):
            dp[i] = dp[i] + dp[i-m]
    return dp[n]
