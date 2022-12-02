import sys
from collections import deque

input = sys.stdin.readline

# m, n = 4,42
# m,n = 100,40021
m,n = map(int, input().split())
queue = deque()
q = deque()

queue.append([n,1])

while queue:
    A,count = queue.popleft()
    # print(A)

    if A == m:
        print(count)
        break

    if A != 0 and A % 2 == 0:
        B = A / 2
        queue.append([B,count+1])
    elif A % 10 == 1:
        B = A // 10
        queue.append([B,count+1])
    else:
        print(-1)
        break

# 4 41 82 821 8211