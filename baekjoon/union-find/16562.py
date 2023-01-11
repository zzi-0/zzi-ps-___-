n, m, k = 5, 3, 10
costs = [10, 10, 20, 20, 30]
friends = [[1, 3],[2, 4],[5, 4]]
visited = [0 for _ in range(n+1)]
sum = 0

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

    if costs[a-1] < costs[b-1]:
        parent[b] = a
    else:
        parent[a] = b

for [f1,f2] in friends:
    union_parent(f1,f2)

for i in range(n):
    f_parent = find_parent(i+1)
    if visited[f_parent] == 0:
        sum += costs[f_parent-1]
        visited[f_parent] = 1

if sum > k:
    print("Oh no")
else:
    print(sum)