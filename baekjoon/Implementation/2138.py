
from collections import deque
n = 3
original = [0,0,0]
result = [0,1,0]
ans = -1

# 000
# 1 -> 110 or 000
# 2 -> 

def change(val):
    if val == 0:
        return 1
    else:
        return 0
    

for i in range(2):
    temp = original[:]
    cnt = 0
    # 첫 번째 전구 켰을 때
    if i == 0:
        cnt += 1
        temp[0] = change(temp[0])
        temp[1] = change(temp[1])
    for j in range(1,n):
        if temp[j-1] != result[j-1]:
            cnt += 1
            temp[j-1] = change(temp[j-1])
            temp[j] = change(temp[j])
            if j != n-1:
                temp[j+1] = change(temp[j+1])
    if temp == result:
        if ans > cnt or ans == -1:
            ans = cnt
    
print(ans)
