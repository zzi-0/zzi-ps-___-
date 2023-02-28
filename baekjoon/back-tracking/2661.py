import sys
from itertools import product

""" n = int(sys.stdin.readline()) """
n = 10
arr = []

def check(arr,idx):
    for i in range(1,(idx//2) +1):
            if arr[-i:] == arr[-2 * i:-i]:
                return False
    else:
        return True

def dfs(idx):
    if not check(arr,idx):
        return
    if idx == n+1:
        print(int("".join(map(str,arr))))
        exit()
    
    for i in range(1,4):
        arr.append(i)
        dfs(idx+1)
        arr.pop()

dfs(1)