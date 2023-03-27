n, k = 3, 15
coins = [1, 5, 12]

dp = [100000] * (k+1)
dp[0] = 0


for i in range(n):
    for j in range(coins[i],k+1):
        dp[j] = min(dp[j],dp[j-coins[i]]+1)
 
if dp[k] == 100000:
    print(-1)
else:
    print(dp[k])
    
