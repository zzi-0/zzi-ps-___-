from collections import deque

n, m = map(int, input().split())
board = []
for _ in range(n):
  board.append(list(map(int, input())))

queue = deque()
queue.append((0,0,1))
end_x = n-1
end_y = m-1
dx = [-1,0,1,0]
dy = [0,1,0,-1]
visited = [[0] * m for _ in range(n)]

while queue:
    x, y, cnt = queue.popleft()

    if x == end_x and y == end_y:
        print(cnt)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1 and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            queue.append((nx,ny,cnt+1))

