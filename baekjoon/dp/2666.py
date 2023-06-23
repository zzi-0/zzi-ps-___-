# 10:00
import sys

input = sys.stdin.readline
n = int(input())
open1,open2 = map(int,input().split())
m = int(input())
order = []
for _ in range(m):
    order.append(int(input()))
ans = 100000000

def dfs(open1,open2,idx,cnt):
    global ans

    if idx == m:
        ans = min(ans,cnt)
        return 

    count1 = abs(open2-order[idx])
    count2 = abs(open1-order[idx])

    dfs(open1,order[idx],idx+1,cnt+count1)
    dfs(order[idx],open2,idx+1,cnt+count2)

dfs(open1,open2,0,0)

print(ans)