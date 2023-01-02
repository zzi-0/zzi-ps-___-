import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

board = []
N,L,R =map(int,input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
ans = 0
dx = [-1,0,1,0]
dy = [0,-1,0,1]
sum = 0
union = []
unionArr = []
i,j = 0,0


def dfs(x,y):
    global sum
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and  L <= abs(board[nx][ny] - board[x][y]) <= R and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            sum += board[nx][ny]
            union.append([nx,ny])
            dfs(nx,ny)


while True:
    unionArr = []
    sumArr = []
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                union.append([i,j])
                sum += board[i][j]
                dfs(i,j)
                unionArr.append(union)
                sumArr.append(sum)
                union = []
                sum = 0
    if len(unionArr) == N * N: break
    else: ans += 1
    for i in range(len(unionArr)):
        for j in range(len(unionArr[i])):
            x,y = unionArr[i][j]
            board[x][y] = sumArr[i] // len(unionArr[i])
            visited[x][y] = 0

print(ans)



