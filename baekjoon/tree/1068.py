import sys
input = sys.stdin.readline

n = 9
nodes = [-1, 0, 0, 2, 2, 4, 4, 6, 6]
del_node = 4
ans = 0

def dfs(delete_id):
    nodes[delete_id] = -2
    for i in range(n):
        if nodes[i] == delete_id and nodes[i] != -2:
            dfs(i)

dfs(del_node)

for i in range(n):
    node = nodes[i]
    if node != -2 and not i in nodes:
        ans += 1

print(ans)