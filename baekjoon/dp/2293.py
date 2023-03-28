n, k = 3, 10
coins = [1, 2, 5]

dp = [0] * (k+1)

dp[0] = 1

for i in range(n):
    for j in range(coins[i],k+1):
        dp[j] = dp[j-coins[i]] + dp[j]
print(dp[k])

# 1 2 3 4 5 6 7 8 9 10
# 1 1 1 1 1 1 1 1 1 1
# 1 2 2 3