n, m, x = 4, 8, 2
roads = [[1, 2, 4],
[1, 3, 2],
[1, 4, 7],
[2, 1, 1],
[2, 3, 5],
[3, 1, 2],
[3, 4, 4],
[4, 2, 3]]

INF = int(1e9)
ans = 0

graph = [[INF for _ in range(n+1)] for _ in range(n+1)]

for i in range(1,n+1):
    graph[i][i] = 0

for [s,e,c] in roads:
    graph[s][e] = c

for k in range(n+1):  
    for i in range(n+1):  
        for j in range(n+1): 
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

for i in range(1,n+1):
    if ans < graph[i][x] + graph[x][i]:
        ans = graph[i][x] + graph[x][i]

print(ans)

