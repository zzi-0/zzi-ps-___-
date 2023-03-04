# 정렬
arr = [[0,0,3],[0,0,46],[0,0,2],[0,0,1]]
arr.sort(key=lambda x:x[2],reverse=True)
print(arr) # [[0, 0, 46], [0, 0, 3], [0, 0, 2], [0, 0, 1]]

# 다익스트라
import heapq

n = 5
m = 9
bus = [[1, 2, 2],[1, 2, 5],
[1, 3, 3],
[1, 4, 1],
[1, 5, 10],
[2, 4, 2],
[3, 4, 1],
[3, 5, 1],
[4, 5, 3]]
start, end = 1, 5
INF = int(1e9)
distance = [INF] * (n+1)
graph = [[] for _ in range(n+1)]

for [s,e,c] in bus:
    graph[s].append((e,c))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop()
        if distance[now] < dist:
            continue
        for s,c in graph[now]:
            cost = dist + c
            if cost < distance[s]:
                distance[s] = cost
                heapq.heappush(q,(cost,s))

dijkstra(start)


# union-find
V = 5
parent = [0 for _ in range(V+1)]

for i in range(5):
    parent[i+1] = i+1

def union_parent(x1,x2):
    p1 = find_parent(x1)
    p2 = find_parent(x2)

    if p1 > p2:
        parent[p1] = p2
    else:
        parent[p2] = p1
        

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


# 플로이드-와샬
board = [[0] * 5 for _ in range(5)]
for k in range(5):
    for i in range(5):
        for j in range(5):
            board[i][j] = min(board[i][j],board[i][k]+board[k][j])

# 배열의 각 원소 2배 
r = [1,2,3,4]
twice_r = map(lambda x:x*2,r)
for t in twice_r:
    print(t) # 2 4 6 8

# 조합
from itertools import combinations
for c in combinations([1,2,3,4],2):
    print(c, end=" ") # (1, 2) (1, 3) (1, 4) (2, 3) (2, 4) (3, 4) 
print("")

# 순열
from itertools import permutations
for i in permutations([1,2,3,4], 2):
    print(i, end=" ") # (1, 2) (1, 3) (1, 4) (2, 1) (2, 3) (2, 4) (3, 1) (3, 2) (3, 4) (4, 1) (4, 2) (4, 3)
print("")

# 중복조합
from itertools import combinations_with_replacement
for cwr in combinations_with_replacement([1,2,3,4], 2):
    print(cwr, end=" ") # (1, 1) (1, 2) (1, 3) (1, 4) (2, 2) (2, 3) (2, 4) (3, 3) (3, 4) (4, 4) 
print("")

# 중복순열
from itertools import product
for i in product(range(3), repeat=3):
    print(i, end=" ") # (0, 0, 0) (0, 0, 1) (0, 0, 2) (0, 1, 0) (0, 1, 1) (0, 1, 2) (0, 2, 0) (0, 2, 1) (0, 2, 2) (1, 0, 0) (1, 0, 1) (1, 0, 2) (1, 1, 0) (1, 1, 1) (1, 1, 2) (1, 2, 0) (1, 2, 1) (1, 2, 2) (2, 0, 0) (2, 0, 1) (2, 0, 2) (2, 1, 0) (2, 1, 1) (2, 1, 2) (2, 2, 0) (2, 2, 1) (2, 2, 2) 
print("")

# 1차원, 2차원 배열 선언
one_d = [0] * 10
print(one_d) # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

two_d = [[0] * 10 for _ in range(2)]
print(two_d) # [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# 큐
from collections import deque
queue = deque()

# 문자열 join, split
string = 'abcd'
s_list = list(string)
print(s_list) # ['a', 'b', 'c', 'd']

j_list = ''.join(s_list)
print(j_list) # abcd