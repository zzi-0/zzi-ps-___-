import sys

N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[0]*N for _ in range(N)]
dp[0][0] = 1
dx = [0,1]
dy = [1,0]


for x in range(N):
    for y in range(N):
        if x == N - 1 and y == N - 1:  
            print(dp[x][y])
            break
        nx = x + board[x][y]
        ny = y + board[x][y]
        if nx < N:
            dp[nx][y] += dp[x][y] 
        if ny < N:
            dp[x][ny] += dp[x][y]

