from collections import deque

n = 6
board = [[5, 4, 3, 2, 3, 4],
[4, 3, 2, 3, 4, 5],
[3, 2, 9, 5, 6, 6],
[2, 1, 2, 3, 4, 5],
[3, 2, 1, 6, 5, 4],
[6, 6, 6, 6, 6, 6]]

ans = 0
fish_size = 2
eat_count = 0
cx, cy = 0, 0

for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            board[i][j] = 0
            cx,cy = i,j
            break

def eat_fish(x, y):
    queue = deque()
    queue.append((x,y,0))
    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[x][y] = 1
    temp = []
    while queue:
        x, y, t = queue.popleft()
        if board[x][y] < fish_size and board[x][y] != 0:
            temp.append((t,x,y))
        else:   
            dx = [-1, 0, 0, 1]
            dy = [0, -1, 1, 0]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and board[nx][ny] <= fish_size and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny, t+1))
    if len(temp) >= 1:
        temp.sort()
        return temp[0]
    else:
        return -1

while True:
    result = eat_fish(cx, cy)
    if result == -1:
        break
    else:
        t,x,y = result
        ans += t
        cx = x
        cy = y
        eat_count += 1
        board[x][y] = 0
        if eat_count == fish_size:
            fish_size = eat_count + 1
            eat_count = 0
print(ans)





