import sys

from collections import deque

input = sys.stdin.readline

N,M = map(int,input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dx = [-1,0,1,0,-1,-1,1,1]
dy = [0,-1,0,1,-1,1,-1,1]

queue = deque()
ans = 0

def bfs(x,y,count):
    visited = [[0 for _ in range(M)] for _ in range(N)]
    queue.clear()
    queue.append((x,y,count))
    global ans
    while len(queue):
        x,y,count = queue.popleft()
        if board[x][y] == 1:
            if ans < count:
                ans = count
            break
        for k in range(8):
            nx = dx[k] + x
            ny = dy[k] + y
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0: 
                visited[nx][ny] = 1
                queue.append((nx,ny,count+1))

for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            bfs(i,j,0)
print(ans)
