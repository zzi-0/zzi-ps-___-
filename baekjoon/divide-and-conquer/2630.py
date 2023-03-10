import sys

input = sys.stdin.readline

n = int(sys.stdin.readline())
confetti = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

white_confetti = 0
blue_confetti = 0

def recursion(start_row,end_row,start_col,end_col,size):
    global white_confetti, blue_confetti
    mid_row = (start_row + end_row) // 2
    mid_col = (start_col + end_col) // 2
    if size == 1:
        if confetti[start_row][start_col] == 0:
            white_confetti += 1
        if confetti[start_row][start_col] == 1:
            blue_confetti += 1
        return
    c = -1
    isSame = True
    for i in range(start_row,end_row):
        for j in range(start_col,end_col):
            if c == -1:
                c = confetti[i][j]
            elif confetti[i][j] != c:
                isSame = False
                break
    if isSame:
        if c == 0:
            white_confetti += 1
        if c == 1:
            blue_confetti += 1
        return
    
    size = size // 2
    recursion(start_row,mid_row,start_col,mid_col,size)
    recursion(mid_row,end_row,start_col,mid_col,size)
    recursion(mid_row,end_row,mid_col,end_col,size)
    recursion(start_row,mid_row,mid_col,end_col,size)

recursion(0,n,0,n,n)
print(white_confetti)
print(blue_confetti)