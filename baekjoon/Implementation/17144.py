import sys
input = sys.stdin.readline

n, m, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
ans = 0
up,down = 0,0

for i in range(n):
    if board[i][0] == -1:
        up = i
        down = i + 1
        break

def diffusion():
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    tmp_arr = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if board[i][j] > 0:
                count = 0
                for k in range(4):
                    nx = dx[k] + i
                    ny = dy[k] + j
                    amount = board[i][j] // 5
                    if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != -1: 
                        tmp_arr[nx][ny] += amount
                        count += 1
                board[i][j] -= amount*count
    
    for i in range(n):
        for j in range(m):
            board[i][j] += tmp_arr[i][j]


def air_up():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = up, 1

    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == up and y == 0:
            break
        if 0 <= nx <= up and 0 <= ny < m:
            board[x][y], before = before, board[x][y]
            x = nx
            y = ny
        else:
            direct += 1


def air_down():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = down, 1

    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == down and y == 0:
            break
        if down <= nx < n and 0 <= ny < m:
            board[x][y], before = before, board[x][y]
            x = nx
            y = ny
        else:
            direct += 1




for i in range(t):
    diffusion()
    air_up()
    air_down()

for i in range(n):
    for j in range(m):
        if board[i][j] > 0:
            ans += board[i][j]

print(ans)






