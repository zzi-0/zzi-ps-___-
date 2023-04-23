n = 6
board = [[0, 0, 0,0,0,0],[0, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0]]
visited = [[0] * n for _ in range(n)]
ans = 0
dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(3)]

dp[0][0][1] = 1
for i in range(2, n):
    if board[0][i] == 0:
        dp[0][0][i] = dp[0][0][i - 1]

for r in range(1, n):
    for c in range(1, n):
        # 대각선 파이프를 추가하는 과정
        if board[r][c] == 0 and board[r][c - 1] == 0 and board[r - 1][c] == 0:
            dp[1][r][c] = dp[0][r - 1][c - 1] + dp[1][r - 1][c - 1] + dp[2][r - 1][c - 1]
            
        # 가로, 세로 파이프를 추가하는 과정
        if board[r][c] == 0:
            dp[0][r][c] = dp[0][r][c - 1] + dp[1][r][c - 1]
            dp[2][r][c] = dp[2][r - 1][c] + dp[1][r - 1][c]


# 최종 결과 출력
print(sum(dp[i][n - 1][n - 1] for i in range(3)))
