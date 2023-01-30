def solution(n, paths, gates, summits):
    answer = []
    INF = int(1e9)
    graph = [[INF for _ in range(n+1)] for _ in range(n+1)]
    path = []
    min_intensity = INF
    min_summit = INF

    for i in range(n+1):
        graph[i][i] = 0

    for [s,e,c] in paths:
        graph[s][e] = c
        graph[e][s] = c
    
    for k in range(n+1):  
        for i in range(n+1):  
            for j in range(n+1): 
                if max(graph[i][k],graph[k][j]) < graph[i][j]:
                    graph[i][j] = max(graph[i][k],graph[k][j])

    
    for g in gates:
        for s in summits:
            path.append((g,s))
    
    for gate,summit in path:
        intensity = max(graph[gate][summit],graph[summit][gate])
        min_intensity = min(min_intensity,intensity)
        answer.append([summit,min_intensity])
    
    for [summit,intensity] in answer:
        if intensity == min_intensity:
            min_summit = min(summit,min_summit)

    return [min_summit,min_intensity]

print(solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5]))
# print(solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4]))