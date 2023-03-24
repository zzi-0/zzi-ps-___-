import sys

input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

dp = [0] * 101
dp[1] = 1
dp[2] = 1
for i in range(3,101):
    dp[i] = dp[i-2] + dp[i-3] 

for a in arr:
    print(dp[a])

