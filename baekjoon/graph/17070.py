import sys

input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
ans = 0

def right(visited,x,y,d):
    if 0 <= x < n and 0 <= y+1 < n and visited[x][y+1] == 0 and board[x][y+1] == 0:
        visited[x][y+1] = 1
        dfs(x,y+1,d)
        visited[x][y+1] = 0

def down(visited,x,y,d):
    if 0 <= x+1 < n and 0 <= y < n and visited[x+1][y] == 0 and board[x+1][y] == 0:
        visited[x+1][y] = 1
        dfs(x+1,y,d)
        visited[x+1][y] = 0

def right_down(visited,x,y,d):
    if 0 <= x+1 < n and 0 <= y+1 < n and visited[x+1][y] == 0 and visited[x+1][y+1] == 0 and visited[x][y+1] == 0 and board[x][y+1] == 0 and board[x+1][y] == 0 and board[x+1][y+1] == 0:
        visited[x][y+1] = 1
        visited[x+1][y+1] = 1
        visited[x+1][y] = 1
        dfs(x+1,y+1,d)
        visited[x][y+1] = 0
        visited[x+1][y+1] = 0
        visited[x+1][y] = 0



def dfs(x,y,d):
    global ans
    if x == n-1 and y == n-1:
        ans += 1
    if d == 0:
        right(visited,x,y,0)
        right_down(visited,x,y,2)
    if d == 1:
        down(visited,x,y,1)
        right_down(visited,x,y,2)
    if d == 2:
        right(visited,x,y,0)
        down(visited,x,y,1)
        right_down(visited,x,y,2)





visited[0][0] = 1
visited[0][1] = 1
dfs(0,1,0)
print(ans)