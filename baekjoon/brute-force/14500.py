
import sys
input = sys.stdin.readline

n, m = 4, 10
board = [[1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
[2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
[1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
[2, 1, 2, 1, 2, 1, 2, 1, 2, 1]]
visited = [[0] * m for _ in range(n)]
ans = 0

def dfs(x,y,count,sum):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    global ans

    if count == 4:
        ans = max(sum,ans)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            dfs(nx,ny,count+1,board[nx][ny]+sum)
            visited[nx][ny] = 0

def exception(x,y):
    global ans
    if y - 1 >= 0 and y + 1 < m and x + 1 < n: # ㅜ
        ans = max(board[x][y]+board[x][y-1]+board[x][y+1]+board[x+1][y],ans)
    
    if y - 1 >= 0 and y + 1 < m and x - 1 >= 0: # ㅗ
        ans = max(board[x][y]+board[x][y-1]+board[x][y+1]+board[x-1][y],ans)
    
    if x - 1 >= 0 and x + 1 < n and y + 1 < m: # ㅏ
        ans = max(board[x][y]+board[x+1][y]+board[x-1][y]+board[x][y+1],ans)
    
    if y - 1 >= 0 and x + 1 < n and x - 1 >= 0: # ㅓ
        ans = max(board[x][y]+board[x+1][y]+board[x-1][y]+board[x][y-1],ans)
    


for i in range(n):
    for j in range(m):
        visited[i][j] = 1 
        dfs(i,j,1,board[i][j])
        visited[i][j] = 0
        exception(i,j)

print(ans)
