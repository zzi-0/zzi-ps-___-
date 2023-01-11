n = 3
m = 3
cities = [[0, 1, 0],
[1, 0, 1],
[0, 1, 0]]
plan = [1, 2, 3]
ans = "YES"
start = -1

parent = [0 for _ in range(n+1)]
for i in range(n):
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

for i in range(n):
    for j in range(n):
        if cities[i][j] == 1:
            union_parent(i+1,j+1)

for p in plan:
    if start == -1:
        start = parent[p]
    if parent[p] != start:
        ans = "NO"

print(ans)