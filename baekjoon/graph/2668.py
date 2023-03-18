import sys
input = sys.stdin.readline

n = int(input())
second = []			
for _ in range(n):
    second.append(int(input()))
tuple = []
filtered_tuple = []
ans = []

for i in range(n):
    tuple.append((i+1,second[i]))

set_second = set(second)

for f,s in tuple:
    if f in set_second:
        filtered_tuple.append((f,s))

def dfs(start,next):
    global visited
    if start == next:
        ans.append(start)
        return
    for f,s in filtered_tuple:
        if f == next and not visited[s]:
            visited[s] = 1
            dfs(start,s)
        
for f,s in filtered_tuple:
    visited = [0] * (n+1)
    dfs(f,s)

print(len(ans))
for a in ans:
    print(a)