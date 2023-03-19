import sys
input = sys.stdin.readline

n,c = map(int, input().split()) 
coordinate = []
for i in range(n):
    coordinate.append(int(input()))
coordinate.sort()
lt = 0
rt = coordinate[n-1] - coordinate[0]
ans = 0

while lt <= rt:
    mid = (lt + rt) // 2
    count = 1
    start = coordinate[0]
    for i in range(1,n):
        if coordinate[i] - start >= mid:
            count += 1
            start = coordinate[i]
    if count >= c:
        lt = mid + 1
        ans = max(ans,mid)
    else:
        rt = mid - 1
print(ans)







