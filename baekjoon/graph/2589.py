from collections import deque

n, m = 5, 7
maps = [['W','L','L','W','W','W','L'],
['L','L','L','W','L','L','L'],
['L','W','L','W','L','W','W'],
['L','W','L','W','L','L','L'],
['W','L','L','W','L','W','W']]
ans = 0

def bfs(start,end):
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    queue = deque()
    queue.append((start,end,0))
    max = 0

    while queue:
        x, y, count = queue.popleft()
        if count > max:
            max = count
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 'L' and visited[nx][ny] == 0:
                queue.append((nx,ny,count+1))
                visited[nx][ny] = 1
    return max

for i in range(n):
    for j in range(m):
        if maps[i][j] == 'L':
            if 0 <= i - 1 and i + 1 < n:
                if maps[i-1][j] == 'L' and maps[i+1][j] == 'L':
                    continue
            if 0 <= j - 1 and j + 1 < m:
                if maps[i][j-1] == 'L' and maps[i][j+1] == 'L':
                    continue
            visited = [[0] * m for _ in range(n)]
            visited[i][j] = 1
            ans = max(ans,bfs(i,j))

print(ans)