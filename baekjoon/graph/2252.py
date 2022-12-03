import sys

input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
plus,minus,multiply,divide = list(map(int, input().split()))

max = -int(1e9)
min = int(1e9)

def dfs(depth,result,plus,minus,multiply, divide):
    global max 
    global min 
    global numbers

    if depth == n:
        if result > max:
            max = result
        if result < min:
            min = result
        return

    if plus:
        dfs(depth+1,result+numbers[depth],plus-1,minus,multiply, divide)
    if minus:
        dfs(depth+1,result-numbers[depth],plus,minus-1,multiply, divide)
    if multiply:
        dfs(depth+1,result*numbers[depth],plus,minus,multiply -1, divide)
    if divide:
        dfs(depth+1,int(result/numbers[depth]),plus,minus,multiply, divide-1)

dfs(1,numbers[0],plus,minus,multiply, divide)
print(max)
print(min)




