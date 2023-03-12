n = 9
m = 11
results = [[2, 1],
[3, 1],
[2, 8],
[2, 9],
[7, 8],
[4, 5],
[6, 7],
[6, 3],
[1, 7],
[6, 2],
[1, 9]]

big_graph = [[] for _ in range(n+1)]
small_graph = [[] for _ in range(n+1)]

for [a,b] in results:
    big_graph[a].append(b)
    small_graph[b].append(a)

def dfs(i):
    visited[i] = 1
    for g in big_graph[i]:
        if not visited[g]:
            visited[g] = 1
            big_dfs(g)
    for s in small_graph[i]:
        if not visited[s]:
            visited[s] = 1
            small_dfs(s)

def small_dfs(i):
    for s in small_graph[i]:
        if not visited[s]:
            visited[s] = 1
            small_dfs(s)

def big_dfs(i):
    for g in big_graph[i]:
        if not visited[g]:
            visited[g] = 1
            big_dfs(g)


for i in range(1,n+1):
    visited = [0] * (n+1)
    dfs(i)
    ans = 0
    for i in range(1,n+1):
        if visited[i] == 0:
            ans += 1
    print(ans)


