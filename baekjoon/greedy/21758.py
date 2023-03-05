import sys

input = sys.stdin.readline
 
n = int(input()) 
data = list(map(int,input().split())) 
#최대값 저장 변수
ans = 0

sum=[] 
sum.append(data[0]) 

for i in range(1,n): 
    sum.append(sum[i-1]+data[i]) 

# 벌통이 가장 왼쪽에 있는 경우
# 벌 1마리는 가장 오른쪽, 벌 1마리는 벌통과 벌 사이 랜덤
for i in range(1,n-1):
    # 다른 한마리의 위치를 i라고 볼 때
    # 가장 오른쪽 벌 sum[n-2] - 다른 벌 1마리 자리 honey[i]
    # 가장 큰 다른 한마리 벌 자리 sum[i-1]
    ans = max(ans, sum[n-2] + sum[i-1] - data[i])

# 벌통이 가장 오른쪽에 있는 경우
# 벌 1마리는 가장 왼쪽, 벌 1마리는 벌통과 벌 사이 랜덤
for i in range(1,n-1):
    # 다른 한마리의 위치를 i라고 볼 때
    # 가장 왼쪽 벌 sum[n-1] - honey[0] - 다른 벌 1마리 자리 honey[i]
    # 가장 큰 다른 한마리 벌 자리 sum[n-1] - sum[i]
    ans = max(ans, sum[n-1] - data[0] - data[i] + sum[n-1] - sum[i]) 


# 벌통이 벌 사이에 위치하는 경우
# 벌 2마리 양쪽에 위치, 벌통은 랜덤 
for i in range(1,n-1):
    # 총합 sum[n-1] - 가장 왼쪽 벌 honey[0] - 가장 오른쪽 벌 honey[n-1] + 벌통 자리 honey[i]
    ans = max(ans, sum[n-2] - data[0] + data[i])


print(ans)