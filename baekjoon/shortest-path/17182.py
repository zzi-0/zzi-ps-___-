import sys
n, k = map(int, sys.stdin.readline().split())
graph = [[*map(int, sys.stdin.readline().split())] for _ in range(n)]

def recursive(pos, cnt, cost):
    global result

    if cnt == n:
        result = min(result, cost)
        return

    for next in range(n):
        if not visit[next]:
            visit[next] = True
            recursive(next, cnt + 1, cost + graph[pos][next])
            visit[next] = False


for a in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][a] + graph[a][j])

visit = [False] * n
result = int(1e9)
visit[k] = True

recursive(k,1,0)
print(result)