import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

dict = {}

def check(target, files):
    if target not in dict:
        return
    for name, type in dict[target]:
        if type == 0:
            files.append(name)
        else:
            check(name, files)
            
n, m = map(int, input().split())
for i in range(n+m):
    p,f,c = input().rstrip().split()
    if p not in dict:
        dict[p] = []
        dict[p].append([f, int(c)])
    else:
        dict[p].append([f, int(c)])

q = int(input())
for _ in range(q):
    folder = input().rstrip().split('/')
    files = []
    check(folder[-1], files)
    print(len(set(files)),len(files))
