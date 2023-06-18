# 1. 사다리 타기 해서 이동하는지 체크 하는 함수 만들기
# 2. 1개부터 3개까지 사다리를 놓을 수 있는 모든 경우의 수 만들기 (단, 가로선 연속 되는지 체크)
from itertools import product
from itertools import combinations
import copy
""" import sys
n, m, h = map(int, sys.stdin.readline().split())  
infos =  [list(map(int, input().split())) for _ in range(m)] """

""" n, m, h = 5, 8, 6
infos = [[1, 1],
[2, 2],
[3, 3],
[4, 4],
[3, 1],
[4, 2],
[5, 3],
[6, 4]] """

n, m, h = 5, 5, 6
infos = [[1, 1],
[3, 2],
[2, 3],
[5, 1],
[6, 5]]

n,m,h = 2, 1, 3
infos = [[1, 2]]

""" n,m,h = 5, 12, 6
infos = [[1, 1],
[1, 3],
[2, 2],
[2, 4],
[3, 1],
[3, 3],
[4, 2],
[4, 4],
[5, 1],
[5, 3],
[6, 2],
[6, 4]] """

graph = [[] for _ in range(n+1)]

for [a,b] in infos:
    if a not in graph[b]:
        graph[b].append((a,b+1))
    if b+1 <= n and a not in graph[b+1]:
        graph[b+1].append((a,b))



def is_possible():
    is_check = True
    for i in range(1,n+1):
        x = i
        y = 1
        while y < h:
            is_cross = False
            print(i,x,y)
            if x <= n:
                for a,b in temp[x]:
                    if y == a:
                        x = b
                        y += 1
                        is_cross = True
                        break
            if not is_cross:
                y += 1
            
        if i == x:
            continue
        else:
            is_check = False
            break
    return is_check

temp = copy.deepcopy(graph)
if is_possible():
    print(0)
else:
    n_number = [ i for i in range(1,h+1)]
    h_number = [ i for i in range(1,n+1)]
    items = [n_number, h_number]
    combi = list(product(*items))

    is_done = False
    for i in range(1,4):
        for c in list(combinations(combi, i)):
            temp = copy.deepcopy(graph)
            for a,b in c:
                if a not in temp[b]:
                    temp[b].append((a,b+1))
                if b+1 <= n and a not in temp[b+1]:
                    temp[b+1].append((a,b))
            if is_possible():
                is_done = True
                break
        if is_done:
            print(i)
            break
    if not is_done:
        print(-1)


