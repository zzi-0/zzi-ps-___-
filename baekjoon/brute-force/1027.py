
import sys
def input(): return sys.stdin.readline().rstrip()

n = int(input())
buildings = list(map(int,input().split()))
grad = [[0] * n for _ in range(n)]

# 각 건물 사이의 기울기 구하기
# grad[i][j]: i 건물과 j 건물 사이의 기울기
for i in range(n):
    for j in range(n):
        if i == j: continue
        grad[i][j] = (buildings[i] - buildings[j]) / (i-j)

# 각 건물에서 볼 수 있는 건물의 갯수 구하기
# max_cnt[A]: A 건물에서 볼 수 있는 건물의 갯수
max_cnt = [0] * n
for i in range(n):
    cnt = 0
    # 왼쪽에서 볼 수 있는 건물 갯수 구하기
    for l in range(i):
        possible = True
        for k in range(l+1,i):
            if grad[k][i] <= grad[l][i]:
                possible = False
        if possible: cnt += 1
    # 오른쪽에서 볼 수 있는 건물 갯수 구하기
    for r in range(i+1,n):
        possible = True
        for k in range(i+1,r):
            if grad[i][k] >= grad[i][r]:
                possible = False
        if possible: cnt += 1
    max_cnt[i] = cnt
print(max(max_cnt))

