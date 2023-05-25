import sys
input = sys.stdin.readline

n = int(input())
costs = [0]*n

for i in range(n):
    costs[i] = list(map(int,input().split()))

for i in range(1, n):
    costs[i][0] = min(costs[i-1][1], costs[i-1][2]) + costs[i][0]
    costs[i][1] = min(costs[i-1][0], costs[i-1][2]) + costs[i][1]
    costs[i][2] = min(costs[i-1][0], costs[i-1][1]) + costs[i][2]

print(min(costs[n-1]))