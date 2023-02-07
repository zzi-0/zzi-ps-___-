import sys

input = sys.stdin.readline
n,m = map(int,input().split())
INF = int(1e9)
[min_dis,first_place,second_place] = [INF, 0, 0]
graph = [[INF for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1
    
for i in range(n):
    graph[i][i] = 0

for k in range(n):  
    for i in range(n):  
        for j in range(n): 
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

for i in range(n):
    for j in range(i,n):
        sum = 0
        for k in range(n):
            if graph[i][k] < graph[j][k]:
                sum += 2*graph[i][k]
            else:
                sum += 2*graph[j][k]
        if min_dis > sum:
            min_dis = sum
            first_place = i + 1
            second_place = j + 1

result = [first_place, second_place, min_dis]
print(*result)