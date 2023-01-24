n = 5
m = 14
bus = [[1, 2, 2],
[1, 3, 3],
[1, 4, 1],
[1, 5, 10],
[2, 4, 2],
[3, 4, 1],
[3, 5, 1],
[4, 5, 3],
[3, 5, 10],
[3, 1, 8],
[1, 4, 2],
[5, 1, 7],
[3, 4, 2],
[5, 2, 4]]

graph = [[0 for _ in range(n)] for _ in range(n)]

for [start,end,cost] in bus:
    if graph[start-1][end-1] == 0:
        graph[start-1][end-1] = cost
    else:
        if graph[start-1][end-1] > cost:
            graph[start-1][end-1] = cost
            

for k in range(n):
    for i in range(n):
        for j in range(n):
            if not i == j and (graph[i][k] + graph[k][j] < graph[i][j] or graph[i][j] == 0):
                if not graph[i][k] == 0 and not graph[k][j] == 0:
                    graph[i][j] = graph[i][k] + graph[k][j]

for row in graph:
    for col in row:
        print(col, end = " ")
    print()