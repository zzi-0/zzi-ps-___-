import sys

input = sys.stdin.readline

T = int(input())
arr = []
for i in range(T):
    arr.append(int(input()))


dp = [0 for i in range(10001)]
dp[1] = 1
dp[2] = 2
dp[3] = 3
for i in range(4,10001):
    dp[i] = 1 + dp[i -2] + (i // 3)
for n in arr:   
    print(dp[n])