import sys
from itertools import combinations
from collections import deque

n = int(sys.stdin.readline().strip())
population = [int(x) for x in sys.stdin.readline().split()]
graph = [[] for _ in range(n+1)]
ans = -1
items = [i for i in range(1, n+1)]

for i in range(n):
    x = list(map(int, input().split()))
    for j in x[1:]:
        graph[i+1].append(j)

def is_connected(have):
    queue = deque()
    queue.append(have[0])
    visited = [have[0]]
    
    while queue:
        start = queue.popleft()
        for g in graph[start]:
            if g in have and g not in visited:
                queue.append(g)
                visited.append(g)
    return len(have) == len(visited)

# population에서 10C2 ~ 10C5까지 모든 조합을 구한다.
for i in range(1, n//2+1):
    combi = list(combinations(items, i))
    for a in combi:
        b = list(set(items) - set(a))
        if is_connected(a) and is_connected(b):
            sum1 = 0
            sum2 = 0
            for k in a:
                sum1 += population[k-1]
            for k in b:
                sum2 += population[k-1]
            if ans == -1 or ans > abs(sum2 - sum1):
                ans = abs(sum2 - sum1)
print(ans)
