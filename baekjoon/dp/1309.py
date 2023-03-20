n = 1000000

dp = [[0,0] for _ in range(n+1)]

dp[0][0] = 1
dp[1][0] = 3
dp[1][1] = 2

for i in range(2,n+1):
    dp[i][1] = (dp[i-1][0] + dp[i-1][1])%9901
    dp[i][0] = (dp[i-1][0] + (dp[i-1][1])*2)%9901
print(dp[n][0])
