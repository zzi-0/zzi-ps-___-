import sys

input = sys.stdin.readline

n,m = map(int,input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for col in range(m)] for row in range(n)]
ans = 0

def dfs(i,j,sum):
    global ans
    if j == m:
        j = 0
        i = i+1
    if i == n:
        if ans < sum:
            ans = sum
        return

    if i+1 < n and j+1 < m:
        if visited[i][j] == 0 and visited[i+1][j] == 0 and visited[i][j+1] == 0:
            visited[i][j] = 1
            visited[i+1][j] = 1
            visited[i][j+1] = 1
            dfs(i,j+1,sum + (board[i][j] * 2) + board[i+1][j] + board[i][j+1])
            visited[i][j] = 0
            visited[i+1][j] = 0
            visited[i][j+1] = 0
    if i-1 >= 0 and j+1 <m:
        if visited[i][j] == 0 and visited[i-1][j] == 0 and visited[i][j+1] == 0:
            visited[i][j] = 1
            visited[i-1][j] = 1
            visited[i][j+1] = 1
            dfs(i,j+1,sum + (board[i][j] * 2) + board[i-1][j] + board[i][j+1])
            visited[i][j] = 0
            visited[i-1][j] = 0
            visited[i][j+1] = 0
    if i+1 < n and j-1 >= 0:
        if visited[i][j] == 0 and visited[i+1][j] == 0 and visited[i][j-1] == 0:
            visited[i][j] = 1
            visited[i+1][j] = 1
            visited[i][j-1] = 1
            dfs(i,j+1,sum + (board[i][j] * 2) + board[i+1][j] + board[i][j-1])
            visited[i][j] = 0
            visited[i+1][j] = 0
            visited[i][j-1] = 0
    if i-1 >= 0 and j-1 >= 0:
        if visited[i][j] == 0 and visited[i-1][j] == 0 and visited[i][j-1] == 0:
            visited[i][j] = 1
            visited[i-1][j] = 1
            visited[i][j-1] = 1
            dfs(i,j+1,sum + (board[i][j] * 2) + board[i-1][j] + board[i][j-1])
            visited[i][j] = 0
            visited[i-1][j] = 0
            visited[i][j-1] = 0
    dfs(i,j+1,sum)

dfs(0,0,0)
print(ans)