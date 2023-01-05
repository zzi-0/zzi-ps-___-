import sys
from collections import deque

""" input = sys.stdin.readline

N,M,T = map(int,input().split())
board = [list(map(int, input().split())) for _ in range(N)] """


N,M,T = 6,6,10
board = [[0, 0, 0, 0 ,1 ,1],
[0, 0 ,0 ,0, 0, 2],
[1 ,1 ,1 ,0 ,1, 0],
[0, 0, 0 ,0 ,0 ,0],
[0 ,1 ,1 ,1, 1, 1],
[0 ,0 ,0 ,0 ,0 ,0]] # 10

N,M,T = 3 ,11 ,20
board = [[0 ,1 ,2 ,1, 1 ,1 ,1 ,1 ,1 ,1 ,1],
[0 ,0, 0, 1, 0, 0, 0, 1 ,1 ,1, 1],
[0 ,1 ,0 ,0 ,0 ,1, 0, 0, 0,0, 0]]  # 14

N,M,T = 3,4,100
board = [[0, 0 ,0 ,0],
[1 ,1 ,1 ,1],
[0, 0, 2, 0]] # Fail

N,M,T = 5 ,11 ,25
board = [[0 ,1 ,2, 0, 0 ,1, 1 ,1 ,1 ,1, 1],
[0 ,1, 1, 1, 0, 0 ,0 ,1 ,1 ,1 ,1],
[0, 0 ,0 ,0 ,0, 1, 0 ,1 ,0 ,0, 0],
[0 ,1 ,1 ,1 ,1 ,1 ,0, 1 ,0, 1, 0],
[0 ,1 ,1, 1, 1 ,0 ,0 ,0 ,0, 1 ,0]] # 20

visited = [[0 for _ in range(M)] for _ in range(N)]

queue = deque()
queue.append((0,0,0))

dx = [-1,0,1,0]
dy = [0,-1,0,1]
ans = -1

while len(queue):
    x,y,count = queue.popleft()
    if x == N - 1 and y == M -1:
        if ans > count or ans == -1:
            ans = count
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
            if board[nx][ny] == 2:
                visited[nx][ny] = 1
                move = count+N-nx-1+M-ny-1+1
                if ans > move or ans == -1:
                    ans = move
            if board[nx][ny] != 1:
                visited[nx][ny] = 1
                queue.append((nx,ny,count+1)) 

if ans <= T and ans != -1:
    print(ans)
else:
    print("Fail")