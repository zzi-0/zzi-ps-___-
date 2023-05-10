import sys
sys.setrecursionlimit(10**8)

pizza = int(sys.stdin.readline().rstrip())
m, n = map(int, sys.stdin.readline().split())
a = [int(sys.stdin.readline().rstrip()) for _ in range(m)]
b = [int(sys.stdin.readline().rstrip()) for _ in range(n)]


a_visited = [0] * (m)
b_visited = [0] * (n)
ans = 0


def dfs(type,c,sum):
    global ans
    if sum == pizza:
        ans += 1
        return
    
    if type == 'a':
        nc = (c + 1) % m
        if a_visited[nc] == 0 and sum + a[nc] <= pizza:
            a_visited[nc] = 1
            dfs('a',nc,sum+a[nc])
            a_visited[nc] = 0
        if 1 not in b_visited:
            for i in range(n):
                nc = (c + i) % n
                if b_visited[nc] == 0 and sum + b[nc] <= pizza:
                    b_visited[nc] = 1
                    dfs('b',nc,sum+b[nc])
                    b_visited[nc] = 0

    
    if type == 'b':
        nc = (c + 1) % n
        if b_visited[nc] == 0 and sum + b[nc] <= pizza:
            b_visited[nc] = 1
            dfs('b',nc,sum+b[nc])
            b_visited[nc] = 0
        if 1 not in a_visited:
            for i in range(m):
                nc = (c + i) % m
                if a_visited[nc] == 0 and sum + a[nc] <= pizza:
                    a_visited[nc] = 1
                    dfs('a',nc,sum+a[nc])
                    a_visited[nc] = 0


for i in range(m):
    a_visited[i] = 1
    dfs('a',i,a[i])
    a_visited[i] = 0

for i in range(n):
    b_visited[i] = 1
    dfs('a',i,b[i])
    b_visited[i] = 0

print(ans)

""" 0 4 7
0 1 7
2 5
3
0 1 2 4 """