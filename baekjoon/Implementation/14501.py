

import sys
input = sys.stdin.readline

n = 3
consulting = [[2, 10],
[5, 20],
[1, 10]]
ans = 0
visited = [0] * n

def dfs(i,sum):
    global ans
    ans = max(ans,sum)
    if i >= n:
        return
    for j in range(i,n):
        if not visited[j]:
            [t,p] = consulting[j]
            if j+t <= n:
                visited[j] = 1
                dfs(j+t,sum+p)
                visited[j] = 0

dfs(0,0)
print(ans)