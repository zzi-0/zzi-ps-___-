import sys
from itertools import combinations
from collections import deque

n = int(sys.stdin.readline().strip())
population = [int(x) for x in sys.stdin.readline().split()]
graph = [[] for _ in range(n+1)]

for i in range(n):
    x = list(map(int, input().split()))
    for j in x[1:]:
        graph[i+1].append(j)

ans = 10000000
items = [i for i in range(1, n+1)] 

def is_connected(visited):
    while queue:
        start = queue.popleft()
        for g in graph[start]:
            if g in have and g not in visited:
                queue.append(g)
                visited.append(g)
    return len(have) == len(visited)

# population에서 10C2 ~ 10C5까지 모든 조합을 구한다.
for i in range(2,n//2+1):
    combi = list(combinations(items, i))
    for c in combi:
        sum1 = 0
        for k in c:
            #print(population[k-1])
            sum1 += population[k-1]
        sum2 = sum(population)  - sum1
        if ans != -1 and ans < abs(sum2 - sum1):
            continue
        queue = deque()
        have = c
        queue.append(have[0])
        if not is_connected([have[0]]):
            continue

        queue = deque()
        have = list(set(items) - set(c))
        queue.append(have[0])
        if is_connected([have[0]]):
            ans = abs(sum2 - sum1)

# 각 조합마다 graph를 탐색하여 연결되어 있는지 확인한다. 단, 최소값 보다 큰것들은 확인하지 않는다.
# 연결되어 있으면 최소값을 갱신한다.


print(ans)

