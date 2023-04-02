import heapq

n, m, end = 4, 8, 4
roads = [[1, 2, 4],
[1, 3, 2],
[1, 4, 7],
[2, 1, 1],
[2, 3, 5],
[3, 1, 2],
[3, 4, 4],
[4, 2, 3]]

ans = 0
INF = int(1e9)
coming_distance = [INF]*(n+1)
graph = [[] for _ in range(n+1)]

for i in range(m):
    s,e,c = roads[i]
    graph[s].append((e,c))

def dijkstra(start,distance):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for s,c in graph[now]:
            cost = dist + c
            if cost < distance[s]:
                distance[s] = cost
                heapq.heappush(q,(cost,s))

# 2(파티) -> 집 : 집 가는 길
dijkstra(end,coming_distance)

# 집 -> 2(파티) : 파티 가는 길
for i in range(1,n+1):
    going_distance = [INF]*(n+1)
    dijkstra(i,going_distance)
    if going_distance[end] + coming_distance[i] > ans:
        ans = going_distance[end] + coming_distance[i]
print(ans)