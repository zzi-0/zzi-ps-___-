import sys
from collections import deque

""" input = sys.stdin.readline

N,M,T = map(int,input().split())
board = [list(map(int, input().split())) for _ in range(N)] """

N,M,T = 3,11,20
board = [[0 ,1 ,2 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1],
[0 ,0, 0, 1, 0, 0 ,0, 1, 1, 1 ,1],
[0 ,1 ,0 ,0 ,0 ,1, 0, 0 ,0 ,0, 0]]

N,M,T = 5 ,11, 25
board = [[0 ,1 ,2 ,0 ,0 ,1 ,1, 1, 1 ,1 ,1],
[0 ,1, 1, 1, 0, 0 ,0 ,1 ,1 ,1, 1],
[0 ,0, 0, 0, 0 ,1 ,0 ,1 ,0, 0, 0],
[0 ,1 ,1 ,1 ,1 ,1 ,0, 1, 0 ,1 ,0],
[0 ,1 ,1 ,1 ,1, 0, 0, 0, 0, 1, 0]]

N,M,T = 6 ,6 ,16
board = [[0 ,0 ,0 ,0 ,1, 1],
[0 ,0 ,0 ,0 ,0, 2],
[1 ,1 ,1 ,0 ,1 ,0],
[0 ,0 ,0, 0, 0 ,0],
[0 ,1 ,1 ,1 ,1 ,1],
[0 ,0 ,0 ,0 ,0 ,0]]

N,M,T = 3 ,4 ,100
board = [[0 ,0, 0 ,0],
[1 ,1 ,1 ,1],
[0, 0 ,2 ,0]]

visited = [[0 for _ in range(M)] for _ in range(N)]

queue = deque()
queue.append((0,0,0,0))

dx = [-1,0,1,0]
dy = [0,-1,0,1]

while len(queue):
    x,y,count,mode = queue.popleft()
    if x == N - 1 and y == M -1:
        if count <= T:
            print(count)
        else:
            print("Fail")
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
            if mode == 1:
                visited[nx][ny] = 1
                queue.append((nx,ny,count+1,1)) 
            if board[nx][ny] == 2:
                visited[nx][ny] = 1
                queue.append((nx,ny,count+1,1)) 
            if board[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx,ny,count+1,0)) 
else:
    print("Fail")