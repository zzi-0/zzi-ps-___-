# 정렬
# NOTE
arr = [[0,0,3],[0,0,46],[0,0,2],[0,0,1]]
arr.sort(key=lambda x:x[2],reverse=True)
arr.sort(key=lambda x:(x[2],x[1]),reverse=True)
print(arr) # [[0, 0, 46], [0, 0, 3], [0, 0, 2], [0, 0, 1]]

# 리스트 관련 메서드
a = [2, 3, 4]

# 추가
a.append(1) # [2, 3, 4, 1]

# 정렬
a.sort() # 오름차순 [1, 2, 3, 4]
a.sort(reverse = True) # 내림차순 [4, 3, 2, 1]
a.reverse() # 뒤집기 [1, 2, 3, 4]

# 삽입 (idx, value)
a.insert(1, 2) # [1, 2, 2, 3, 4]

# 개수
a.count(2) # 2

# 제거 ( 앞에서 가장 먼저 나오는 하나만 제거)
a.remove(2) # [1, 2, 3, 4]

# 다익스트라
# NOTE
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
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for s,c in graph[now]:
            cost = dist + c
            if cost < distance[s]:
                distance[s] = cost
                heapq.heappush(q,(cost,s))

dijkstra(start)

# union-find
# NOTE
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

# 리스트 컴프리헨션
array = [i for i in range(20) if i % 2 == 1]
array = [i*i for i in range(1,10)]

# 큐
from collections import deque
queue = deque()

# 문자열 join, split
string = 'abcd'
s_list = list(string)
print(s_list) # ['a', 'b', 'c', 'd']

j_list = ''.join(s_list)
print(j_list) # abcd

# 문자열 자르기
a = "ABCDEF"

print(a[2:4]) #CD

# dict
dict = {}
dict['name'] = 'zzi'
dict['age'] = 25
name = dict.get('name')
del dict['name']
for key in dict:
    print(key,dict[key])

# set
s = set()
s.add('a')
s.update(['a', 'b', 'c']) # 여러 개의 값 추가
s.remove('b')
print(s)

# 컴퓨터는 2진수 체계이기 때문에 실수 덧셈을 정확히 하지 못한다. 보통 5째 자리에서 반올림 하면된다.
a = 0.3 + 0.6
print(round(a,4))

# 나눗셈 관련
a = 7
b = 3
# 나누기
print(a / b)
# 나머지
print(a % b)
# 몫
print(a // b)

# copy 
import copy 

arr1 = [1, 2, [99, 88, 77], 3]
arr2 = copy.deepcopy(arr1) 

# 수학
import math

print(math.factorial(5)) # 5 팩토리얼 출력
print(math.sqrt(7)) # 7의 제곱근 출력
print(math.gcd(21,14)) # 21과 14의 최대 공약수 , 7

# 합
sum([1, 2, 3]) # 6

# 최소값, 최대값
min(1, 2, 3) # 1
max(1, 2, 3) # 3

# Counter => 등장 횟수를 세는 기능을 제공한다.
from collections import Counter

counter = Counter([1, 1, 1, 2, 2, 3])

print(counter[1])
print(counter[2])
print(counter[3])


# 2차원 배열 돌리기
def rotated(sticker):
    list_of_tuples = zip(*sticker[::-1])
    return [list(elem) for elem in list_of_tuples]

# 루프문 탈출하기
class LoopBreak(Exception):
    pass

for index in range(5):
    try:
        for i in range(n-r+1):
            for j in range(m-c+1):
                # 어떤 조건
                if True:
                    raise LoopBreak()
    except LoopBreak:
        break