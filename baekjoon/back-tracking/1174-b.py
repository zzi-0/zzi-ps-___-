import sys
from itertools import combinations

# n = int(sys.stdin.readline())
n = 19
arr = []
result = set()

def dfs():
    global result
    global arr
    if arr:
        result.add(int("".join(map(str, arr))))
    for i in range(10):
        if not arr or arr[-1] > i:
            arr.append(i)
            dfs()
            arr.pop()

dfs()
result = list(result)
result.sort()

if len(result) >= n: print(result[n-1])
else: print(-1)

