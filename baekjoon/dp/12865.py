import sys

input = sys.stdin.readline

""" n, k = map(int, input().split())
stuff = [list(map(int, input().split())) for _ in range(n)]
"""
n,k = 4, 6
stuff = [[2, 4],
[3, 5],
[6, 9],
[1, 1]]

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,k+1):
        [w,v] = stuff[i-1]
        if j - w >= 0:
            dp[i][j] = max(dp[i-1][j-w]+v,dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
            

for d in dp:
    print(d)
print(dp[n][k])
