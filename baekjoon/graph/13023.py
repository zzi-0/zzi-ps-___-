import sys
input = sys.stdin.readline

""" n,m = map(int,input().split())
relation = [list(map(int, input().split())) for _ in range(m)]  """
n,m = 5, 5
relation = [[0, 1],
[1, 2],
[2, 3],
[3, 0],
[1, 4]]

is_relation = False
graph = [[] for _ in range(n)]

for [r1, r2] in relation:
    graph[r1].append(r2)
    graph[r2].append(r1)


def dfs(v,level):
    global is_relation
    if level == 5:
        is_relation = True
        return
    else:
        for r in graph[v]:
            if not visited[r]:
                visited[r] = 1
                dfs(r,level+1)
                visited[r] = 0

for i in range(n):
    if is_relation:
        break
    visited = [0] * n
    visited[i] = 1
    dfs(i,1)

if is_relation:
    print("1")
else:
    print("0")
