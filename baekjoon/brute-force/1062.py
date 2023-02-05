import sys
input = sys.stdin.readline

n, k = 3, 6
words = ['antarctica',
'antahellotica',
'antacartica']
learn = [0] * 26
max = 0

for c in ('a', 'c', 'i', 'n', 't'):
    learn[ord(c) - ord('a')] = 1

def dfs(idx,level):
    global max
    if level == k-5:
        cnt = 0
        for word in words:
            readable = True
            for c in word:
                if not learn[ord(c) - ord('a')]:
                    readable = False
                    break
            if readable:
                cnt += 1
        if max < cnt:
            max = cnt
        return
    else:
        for i in range(idx,26):
            if not learn[i]:
                learn[i] = 1
                dfs(i,level+1)
                learn[i] = 0

if k < 5:
    print(0)
elif k == 26:
    print(n)
else:
    dfs(0,0)
    print(max)

