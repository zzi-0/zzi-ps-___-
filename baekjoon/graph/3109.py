import sys
input = sys.stdin.readline
r, c = map(int,input().split())
visited = [[0 for _ in range(c)] for _ in range(r)]
board = [list(input().strip()) for _ in range(r)]

answer = 0
def dfs(x, y):
    if y == c-1:
        return True
    for dx in [-1,0,1]:
        nx = x + dx
        ny = y + 1
        if 0 <= nx < r and 0 <= ny < c:
            if board[nx][ny] != "x" and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                if dfs(nx, ny):
                    return True
    return False


visited = [[0 for _ in range(c)] for _ in range(r)]
for i in range(r):
    if dfs(i,0): 
        answer += 1
print(answer)


""" r, c  = 6, 10
board = [['.','.','x','.','.','.','.','.','.','.'],
['.','.','.','.','.','X','.','.','.','.'],
['.','X','.','.','.','.','X','.','.','.'],
['.','.','.','X','.','.','.','X','X','.'],
['.','.','.','.','.','.','.','.','.','.'],
['.','.','.','.','x','.','.','.','.','.']] """
