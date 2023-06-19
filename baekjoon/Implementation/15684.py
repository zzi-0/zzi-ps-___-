import sys
read = sys.stdin.readline

n, m, h = map(int, read().split())
board = [[0 for _ in range(n+1)] for _ in range(h+1)]
candidates = []
ans = 4
for _ in range(m):
    t1, t2 = map(int, read().split())
    board[t1][t2] = 1

# (3,4),(4,1),(5,3)
def check():
    for start in range(1,n+1): 
        k = start 
        for j in range(1,h+1):
            if board[j][k]: 
                k += 1 
            elif board[j][k - 1]: 
                k -= 1 
        if k != start: 
            return False 
    return True


def dfs(cnt,idx):
    global ans
    if check():
        ans = min(ans, cnt)
        return
    if cnt >= 3 or ans <= cnt:
        return
    for i in range(idx,len(candidates)):
        a,b = candidates[i] 
        board[a][b] = 1
        dfs(cnt+1,i+1)
        board[a][b] = 0

for i in range(1, h+1):
    for j in range(1, n):
        if board[i][j] == 0 and board[i][j-1] == 0 and board[i][j+1] == 0:
            candidates.append([i, j])

dfs(0,0)

if ans == 4:
    print(-1)
else:
    print(ans)
