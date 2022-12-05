import sys

input = sys.stdin.readline

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
a,b,c = 0,0,0

def solution(x,y,n):
    global a,b,c
    for i in range(x,x+n):
        for j in range(y,y+n):
            if paper[i][j] != paper[x][y]:
                num1 = n // 3 * 1
                num2 = n // 3 * 2
                solution(x,y,n//3)
                solution(x,y+num1,n//3)
                solution(x,y+num2,n//3)
                solution(x+num1,y,n//3)
                solution(x+num1,y+num1,n//3)
                solution(x+num1,y+num2,n//3)
                solution(x+num2,y,n//3)
                solution(x+num2,y+num1,n//3)
                solution(x+num2,y+num2,n//3)
                return
    if paper[x][y] == -1:
        a+=1
    if paper[x][y] == 0:
        b+=1
    if paper[x][y] == 1:
        c+=1


solution(0,0,N)
print(a)
print(b)
print(c)



