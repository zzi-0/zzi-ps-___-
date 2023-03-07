import sys
input = sys.stdin.readline

n,m = map(int,input().split())
board = []
r,c,d = map(int,input().split())

for _ in range(n):
    board.append(list(map(int,input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ans = 0

""" 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
2-1. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
2-2. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
3-1. 반시계 방향으로 90도 회전한다.
3-2. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
3-3. 1번으로 돌아간다. """

while True:
    # 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
    if board[r][c] == 0:
        board[r][c] = -1
        ans += 1

    # 청소되지 않은 빈 칸
    is_not_cleaning = False
    for i in range(4):
        nx = r + dx[i]
        ny = c + dy[i]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
            is_not_cleaning = True
            break

    # 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
    if not is_not_cleaning:
        r -= dx[d]
        c -= dy[d]
        if 0 > r or r >= n or 0 > c or c >= m or board[r][c] == 1:
            break
    # 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
    else:
        d = (d + 3) % 4
        r += dx[d]
        c += dy[d]
        if 0 <= r < n and 0 <= c < m and board[r][c] == 0:
            continue
        else:
            r -= dx[d]
            c -= dy[d]





print(ans)