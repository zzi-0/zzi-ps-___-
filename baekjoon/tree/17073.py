import sys
input=sys.stdin.readline

n, w = 5, 20
cnt = 0
tree=[[] for _ in range(n+1)]

for i in range(n-1):
    a,b=map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
    

for i in range(2, len(tree)):
    if len(tree[i]) == 1:
        cnt += 1

print(w/cnt)
