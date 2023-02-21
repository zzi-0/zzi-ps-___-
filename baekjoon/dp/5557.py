import sys

input = sys.stdin.readline

""" n, k = map(int, input().split())
stuff = [list(map(int, input().split())) for _ in range(n)]
"""

n = 40
nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1, 1, 1, 0 ,0 ,1, 1]
""" n = 6
nums = [0, 0, 0, 1, 7, 8] """
value = nums[n-1]

dp = [[0 for _ in range(21)] for _ in range(n)]
dp[1][nums[0]] = 1



for i in range(1,n):
    for j in range(0,21):
        num = nums[i-1]
        if j - num >= 0:
            dp[i][j] = dp[i][j] + dp[i-1][j-num]
        if j + num <= 20:
            dp[i][j] = dp[i][j] + dp[i-1][j+num]
            

print(dp[n-1][value])