n = 1
m = 0
vip = []
ans = 1
vip.insert(0,0)
vip.append(n+1)

if n == 1:
    print(1)
else:
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2]

    for i in range(1,m+2):
        if vip[i]-vip[i-1]-1 != 0:
            ans *= dp[vip[i]-vip[i-1]-1]
        
    print(ans)
