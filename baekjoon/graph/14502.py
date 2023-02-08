from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int,input().split())
map = [list(map(int, input().split())) for _ in range(m)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ans = 0

virus = []
for i in range(n):
    for j in range(m):
        if map[i][j] == 2:
            virus.append([i,j])

def bfs(map):
    global ans
    queue = deque()
    cnt = 0
    copy_map = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            copy_map[i][j] = map[i][j]

    for v in virus:
        queue.append(v)

    while len(queue):
        [x,y] = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and copy_map[nx][ny] == 0:
                copy_map[nx][ny] = 2
                queue.append([nx,ny])

    for i in range(n):
        for j in range(m):
            if copy_map[i][j] == 0:
                cnt += 1
    if ans < cnt:
        ans = cnt



for a in range(0,n*m-2):
    for b in range(a+1,n*m-1):
        for c in range(b+1,n*m):
            a_col = a // m
            a_row = a % m
            b_col = b // m
            b_row = b % m
            c_col = c // m
            c_row = c % m
            if map[a_col][a_row] == 0 and map[b_col][b_row] == 0 and map[c_col][c_row] == 0:
                map[a_col][a_row] = 1
                map[b_col][b_row] = 1
                map[c_col][c_row] = 1
                bfs(map)
                map[a_col][a_row] = 0
                map[b_col][b_row] = 0
                map[c_col][c_row] = 0
print(ans)