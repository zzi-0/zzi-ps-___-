import sys
from collections import deque

input = sys.stdin.readline

S = int(input())
dp = [[-1]* (S+1) for _ in range(S+1)]
dp[1][0] = 0
queue = deque()
queue.append((0,1))

while len(queue):
    s,c = queue.popleft()
    if s == S:
        print(dp[s][c] + 1)
        break
    if dp[s][s] == -1:
        dp[s][s] = dp[s][c] + 1
        queue.append((s,s))
    if s+c <= S and dp[s+c][c] == -1:
        dp[s+c][c] = dp[s][c] + 1
        queue.append((s+c, c))
    if s-1 >= 0 and dp[s-1][c] == -1:
        dp[s-1][c] = dp[s][c] + 1
        queue.append((s-1, c))

