import sys

input = sys.stdin.readline

N = 4
foods = [[1,7],[2,6],[3,8],[4,9]]
ans = 1000000000

def dfs(level,arr):
    if level == N:
        if len(arr) >= 1:
            global ans
            add = 0
            mul = 1
            for i in range(len(arr)):
                add += arr[i][1] 
                mul *= arr[i][0]
            if abs(mul - add) < ans:
                ans = abs(mul - add)
    else:
        dfs(level+1,arr)
        arr.append(foods[level])
        dfs(level+1,arr)
        arr.pop()

dfs(0,[])
print(ans)