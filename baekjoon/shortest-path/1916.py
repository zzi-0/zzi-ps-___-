import heapq

n = 5
m = 9
bus = [[1, 2, 2],[1, 2, 5],
[1, 3, 3],
[1, 4, 1],
[1, 5, 10],
[2, 4, 2],
[3, 4, 1],
[3, 5, 1],
[4, 5, 3]]
start, end = 1, 5

INF = int(1e9)

distance = [INF]*(n+1)

graph = [[] for _ in range(n+1)]

for i in range(m):
    s,e,c = bus[i]
    graph[s].append((e,c))



def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)
print(distance[end])