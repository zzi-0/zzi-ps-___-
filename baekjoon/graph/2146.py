import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**6)


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
border = [[0 for _ in range(n)] for _ in range(n)]
count = 1
dx = [-1,0,1,0]
dy = [0,1,0,-1]
ans = 1000000000

queue = deque()

# 서로 다른 섬으로 만들기
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


# 가장자리 만들기 (시간 초과 안되게 하기)
for i in range(n):
    for j in range(n):
        if board[i][j] != 0:
            is_exist_zero = False
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                if 0 <= ni < n and 0 <= nj < n and board[ni][nj] == 0:
                    is_exist_zero = True
                    break
            if is_exist_zero:
                border[i][j] = 1

# 가장자리이면서 섬이면 bfs 돌면서 최소 거리 찾기
for i in range(n):
    for j in range(n):
        if border[i][j] == 1:
            b_visited = [[0 for _ in range(n)] for _ in range(n)]
            queue = deque()
            b_visited[i][j] = 1
            queue.append((i,j,0))
            num = board[i][j]

            while len(queue):
                x,y,cnt = queue.popleft()

                if num != board[x][y] and board[x][y] != 0:
                    ans = min(ans,cnt-1)
                    break
                
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if 0 <= nx < n and 0 <= ny < n and b_visited[nx][ny] == 0:
                        b_visited[nx][ny] = 1
                        queue.append((nx,ny,cnt+1))
    

print(ans)