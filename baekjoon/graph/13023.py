import sys
input = sys.stdin.readline

""" n,m = map(int,input().split())
relation = [list(map(int, input().split())) for _ in range(m)]  """
n,m = 6, 5
relation = [[0, 1],
[0, 2],
[0, 3],
[0, 4],
[0, 5]]

is_relation = False
graph = [[] for _ in range(n)]

for [r1, r2] in relation:
    graph[r1].append(r2)
    graph[r2].append(r1)


def dfs(v,level):
    if level == 5:
        return True
    else:
        for r in graph[v]:
            if not visited[r]:
                visited[r] = 1
                if dfs(r,level+1):
                    return True
                visited[r] = 0
    return False

for i in range(n):
    visited = [0] * n
    visited[i] = 1
    if dfs(i,1):
        print('1')
        break
else:
    print('0')
