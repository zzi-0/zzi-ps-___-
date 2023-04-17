import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())

board = [[0] * m for _ in range(n)]
ans = 0

# 1. 스티커 겹치거나 노트북 벗어나지 않도록 붙이기 , 가장 위쪽이면서 왼쪽 
# 2. 90도 회전, 180도 회전, 270회전 해서 도전해보기

class LoopBreak(Exception):
    pass

def attach(i,j,r,c):
    global ans
    for x in range(r):
        for y in range(c):
            if sticker[x][y] == 1:
                board[i+x][j+y] = 1
                ans += 1

def rotated(sticker):
    list_of_tuples = zip(*sticker[::-1])
    return [list(elem) for elem in list_of_tuples]

def check(i,j):
    is_attach = True
    for x in range(r):
        for y in range(c):
            if sticker[x][y] == 1 and board[i+x][j+y] == 1:
                is_attach = False
                break
    return is_attach


for index in range(k):
    r, c = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(r)]
    # [r,c, sticker] = stickers[index]
    d = 0
    while d < 4:
        try:
            if d != 0:
                sticker = rotated(sticker)
                r = len(sticker)
                c = len(sticker[0])
            for i in range(n-r+1):
                for j in range(m-c+1):
                    is_attach = check(i,j)
                    if is_attach:
                        attach(i,j,r,c)
                        raise LoopBreak()
            d+=1
        except LoopBreak:
            break

print(ans)
