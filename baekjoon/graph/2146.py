import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**6)


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
count = 1
dx = [-1,0,1,0]
dy = [0,1,0,-1]
ans = 1000000000

queue = deque()


def distinguish(x,y,count):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 1 and visited[nx][ny] == 0:
            board[nx][ny] = count
            visited[nx][ny] = 1
            distinguish(nx,ny,count)


for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and board[i][j] == 1:
            count += 1
            board[i][j] = count
            visited[i][j] = 1
            distinguish(i,j,count)



for i in range(n):
    for j in range(n):
        if board[i][j] != 0:
            b_visited = [[0 for _ in range(n)] for _ in range(n)]
            queue = deque()
            b_visited[i][j] = 1
            queue.append((i,j,0,board[i][j]))

            while len(queue):
                x,y,cnt,num = queue.popleft()

                if num != board[x][y] and board[x][y] != 0:
                    ans = min(ans,cnt-1)
                    # print(cnt)
                    break
                
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if 0 <= nx < n and 0 <= ny < n and b_visited[nx][ny] == 0:
                        b_visited[nx][ny] = 1
                        queue.append((nx,ny,cnt+1,num))
    

print(ans)