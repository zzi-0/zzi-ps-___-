from sys import stdin


N,M = map(int, stdin.readline().split())
board = [[0] * (N + 1)]

for _ in range(N):
    nums = [0] + [int(x) for x in stdin.readline().split()]
    board.append(nums)


for i in range(N+1):
    for j in range(N):
        board[i][j+1] += board[i][j]


for j in range(N+1):
    for i in range(N):
        board[i+1][j] += board[i][j]


for i in range(M):
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    print(board[x2][y2] - board[x1-1][y2] - board[x2][y1-1] + board[x1-1][y1-1])