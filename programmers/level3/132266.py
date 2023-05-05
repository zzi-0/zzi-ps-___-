from collections import deque

# 시간초과를 해결한 방법 2가지!
# 1. 방문한 road인지 체크 => if cost[e] == -1
# 2. sources 만큼 돌려서 destination의 거리를 구했는데, 바꾸어서 destination에서 sources만큼의 거리를 구하기 => (len(sources)) -> 1로 시간 단축

def solution(n, roads, sources, destination):
    graph = [[] for _ in range(n+1)]
    for [s,e] in roads:
        graph[s].append(e)
        graph[e].append(s)

    queue = deque()
    queue.append(destination)
    cost = [-1] * (n+1)
    cost[destination] = 0

    while queue:
        q = queue.popleft()
        for e in graph[q]:
            if cost[e] == -1:
                cost[e] = cost[q] + 1
                queue.append(e)
            
    return [cost[i] for i in sources]

print(solution(3, [[1, 2], [2, 3]],[2, 3], 1))
print(solution(5, [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]], [1, 3, 5], 5))