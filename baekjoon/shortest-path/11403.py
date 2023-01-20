import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

def bfs(x):
    queue = deque()
    queue.append(x) 
    visited = [0 for _ in range(N)]
    while len(queue):
        q = queue.pop()
        for i in range(N):
            if matrix[q][i] and not visited[i]:
                matrix[x][i] = 1
                visited[i] = 1
                queue.append(i)

for i in range(N):
    bfs(i)

for row in matrix:
    for col in row:
        print(col, end = " ")
    print()