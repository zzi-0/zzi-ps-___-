# -*- coding: utf-8 -*- 
import sys
input = sys.stdin.readline

""" N, S = map(int,input().split())
numbers = list(map(int,input().split())) """

N,S = 10,15
numbers = [5,1,3,5,10,7,4,9,2,100]
i,j,ans,sum = 0,0,-1,0

while True:
    print(i,j,sum)
    if i == N:
        break
    # 합작으면 j 증가 시키기
    if sum < S:
        if j < N: 
            sum += numbers[j]
            j += 1
        else:
            break
    # 합 크면 i 증가 시키기
    else:
        len = j - i
        if len < ans or ans == -1:
            ans = len
        sum -= numbers[i]
        i += 1

if ans == -1:
    print(0)
else: 
    print(ans)