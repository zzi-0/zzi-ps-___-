import sys
from collections import deque
input = sys.stdin.readline

sys.setrecursionlimit(10**8)

n, k = map(int, input().split())
words = [input()[4:-4] for _ in range(n)]
learn = [0] * 26
max = 0

for c in ('a', 'c', 'i', 'n', 't'):
    learn[ord(c) - ord('a')] = 1

def get_readable_cnt():
    cnt = 0
    global max
    for word in words:
        readable = True
        for c in word:
            if not learn[ord(c) - ord('a')]:
                readable = False
                break
        if readable:
            cnt += 1
    return cnt
    
def dfs(level):
    global max
    if level == k-5:
        cnt = get_readable_cnt()
        if max < cnt:
            max = cnt
        return
    else:
        for i in range(26):
            if not learn[i]:
                learn[i] = 1
                dfs(level+1)
                learn[i] = 0

if k < 5:
    print(0)
elif k == 26:
    print(n)
else:
    dfs(0)
    print(max)