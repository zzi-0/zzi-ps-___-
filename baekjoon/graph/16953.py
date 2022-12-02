import sys
from collections import deque

input = sys.stdin.readline

# m, n = 4,42
# m,n = 100,40021
m,n = map(int, input().split())
queue = deque()

queue.append([m,1])

while queue:
    A,count = queue.popleft()

    if A == n:
        print(count)
        break
    if A > n:
        continue
    
    B = A * 2
    queue.append([B,count+1])
    
    B = int(str(A) + "1")
    queue.append([B,count+1])

else: 
    print(-1)