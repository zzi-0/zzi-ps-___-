import sys
from collections import deque

input = sys.stdin.readline

h,w = map(int, input().split())
blockHeight = list(map(int, input().split()))

ans = 0
board =  [[0]*w for _ in range(h)]


for i in range(len(blockHeight)):
    for j in range(blockHeight[i]):
        board[j][i] = 1


for i in range(h):
    left = False
    right = False
    acc = 0
    for j in range(w):
        if board[i][j] == 0:
            if j-1 >= 0 and board[i][j-1] == 1:
                right = False
                left = True
            if j+1 < w and board[i][j+1] == 1:
                right = True
            if left and right:
                left = False
                right = False
                acc += 1
                ans += acc
                acc = 0
            if left and j+1 < w and board[i][j+1] == 0:
                acc += 1

print(ans)

