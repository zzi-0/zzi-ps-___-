from itertools import product
n, k, p, x = 48, 2, 5, 35

ans = 0
check = [[1,1,1,0,1,1,1],
    [0,0,1,0,0,0,1],
    [0,1,1,1,1,1,0],
    [0,1,1,1,0,1,1],
    [1,0,1,1,0,0,1],
    [1,1,0,1,0,1,1],
    [1,1,0,1,1,1,1],
    [0,1,1,0,0,0,1],
    [1,1,1,1,1,1,1],
    [1,1,1,1,0,1,1]]

for i in range(1,n+1):
    if i == x:
        continue
    cnt = 0
    f = x
    t = i
    for j in range(k):
        for b in range(7):
            if check[f%10][b] != check[t%10][b]:
                cnt += 1
        f = int(f/10)
        t = int(t/10)
    if cnt <= p:
        ans += 1

print(ans)