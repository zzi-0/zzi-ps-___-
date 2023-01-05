import sys
from collections import deque

input = sys.stdin.readline

N,M = 5,7
board = [[0, 0, 0, 0, 0, 0, 0],
[0, 3, 6, 0, 6, 7, 0],
[0, 3, 0, 0, 0, 10, 0],
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0]]

""" N,M = map(int,input().split())
board = [list(map(int, input().split())) for _ in range(N)] """

""" N,M = 4,4
board = [[0 ,0 ,0 ,0],
[0 ,1 ,1 ,0],
[0 ,1 ,1 ,0],
[0 ,0 ,0 ,0]] """

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 0

    
def get_group_count():
    count = 0
    visited = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0 and visited[i][j] == 0:
                count += 1
                queue = deque()
                queue.append((i,j))
                while len(queue):
                    x,y = queue.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] > 0 and visited[nx][ny] == 0:
                            queue.append((nx,ny))
                            visited[nx][ny] = 1
    return count



def melt():
    global ans
    ans+=1
    melted = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if board[i][j] == 0:
                        melted[i][j] = 1
                    if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0 and melted[nx][ny] == 0 and board[i][j] > 0:
                        board[i][j] = board[i][j] - 1




while True:
    count = get_group_count()
    if count >= 2:
        print(ans)
        break
    elif count == 0:
        print(0)
        break
    else:
        melt()


