from __future__ import print_function
from collections import deque
import sys

input = sys.stdin.readline

N,M = map(int,input().split())
board = [list(map(int, input().split())) for _ in range(N)]

visited = [[0 for _ in range(M)] for _ in range(N)]
answer = [[0 for _ in range(M)] for _ in range(N)]
queue = deque()
isStop = False
for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            queue.append([i,j])
            visited[i][j] = 1
            isStop = True
            
    if isStop:
        break


dx = [-1,0,1,0]
dy = [0,-1,0,1]

while len(queue):
    [x,y] = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 1 and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            answer[nx][ny] = answer[x][y] + 1
            queue.append([nx,ny]) 

for i in range(N):
    for j in range(M):
        if answer[i][j] == 0 and board[i][j] == 1:
            print(-1,end=" ")
        else:
            print(answer[i][j],end=" ")
    print()