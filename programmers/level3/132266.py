from collections import deque
import heapq

def solution(n, roads, sources, destination):
    answer = []
    graph = [[] for _ in range(n+1)]

    for [s,e] in roads:
        graph[s].append(e)
        graph[e].append(s)

    for source in sources:
        queue = deque()
        queue.append((source,0))
        while queue:
            q,cost = queue.popleft()
            if q == destination:
                answer.append(cost)
                break

            for e in graph[q]:
                queue.append((e,cost+1))
        else:
            answer.append(-1)


            
    return answer

print(solution(3,[[1, 2], [2, 3]],[2, 3],1))
print(solution(5,[[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]],[1, 3, 5],5))