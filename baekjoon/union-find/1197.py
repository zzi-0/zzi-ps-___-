import sys
input = sys.stdin.readline

V,E = 3,3
infos = [[1, 2, 4],
[2, 3, 2],
[1, 3, 3]]

""" V,E = map(int,input().split())
infos = [list(map(int, input().split())) for _ in range(E)] """
infos.sort(key=lambda x:x[2])
ans = 0

parent = [0 for _ in range(V+1)]
for i in range(V):
    parent[i+1] = i+1

def find_parent(x):
    global parent
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a,b):
    global parent
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for [v1,v2,cost] in infos:
    if find_parent(v1) != find_parent(v2):
        ans += cost
        union_parent(v1,v2)
print(ans)