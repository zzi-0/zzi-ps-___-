import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m = map(int,input().split())
sets = [list(map(int, input().split())) for _ in range(m)]

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


for [op,num1,num2] in sets:
    if op == 0:
        union_parent(num1,num2)
    if op == 1:
        num1_parent = find_parent(num1)
        num2_parent = find_parent(num2)
        if num1_parent == num2_parent:
            print("YES")
        else:
            print("NO")

