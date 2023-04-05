import sys
from collections import deque

input = sys.stdin.readline

r, c = 3, 6
board = [['H','F','D','F','F','B'],
['A','J','H','G','D','H'],
['D','G','A','G','E','H']]

r, c = 5, 5
board = [['I','E','F','C','J'],['F','H','F','K','C'],['F','F','A','L','F'],['H','F','G','C','F'],['H','M','C','H','H']]


check = [0]*26
queue = deque()
dx = [-1,0,1,0]
dy = [0,1,0,-1]
check[ord(board[0][0])-65] = 1
ans = 0


def dfs(x,y,cnt):
    global ans
    if cnt > ans:
        ans = cnt
    
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < r and 0 <= ny < c and not check[ord(board[nx][ny]) - 65]:
            check[ord(board[nx][ny]) - 65] = 1
            dfs(nx,ny,cnt+1)
            check[ord(board[nx][ny]) - 65] = 0

dfs(0,0,1)
print(ans)


