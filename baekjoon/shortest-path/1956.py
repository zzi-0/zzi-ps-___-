
V, E = 3, 4
roads = [[1, 2, 1],
[3, 2, 1],
[1, 3, 5],
[2, 3, 2]]
INF = int(1e9)
ans = INF


graph = [[INF for _ in range(V+1)] for _ in range(V+1)]

for i in range(V):
    graph[i][i] = 0

for [s,e,c] in roads:
    graph[s][e] = c

for k in range(V+1):  
    for i in range(V+1):  
        for j in range(V+1): 
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

for i in range(1,V+1):
    for j in range(i+1,V+1):
        ans = min(ans,graph[i][j] + graph[j][i])

if ans == INF:
    print(-1)
else:
    print(ans)