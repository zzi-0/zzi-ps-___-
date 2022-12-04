import sys

input = sys.stdin.readline

N, r, c = map(int,input().split())
n = 2 ** N
cnt = 0

def z_search(row,col,n):
    global cnt
    # 탐색 증인 배열 중에 찾는 좌표가 없다면 좌표에 크기를 더한다.
    if not row <= r < row+n and col <= c <= col+n:
        cnt += n**2
        return 

    if n > 2:
        n//=2
        # 1/2/3/4사분면을 재귀적으로 탐색
        z_search(row,col,n)
        z_search(row,col+n,n)
        z_search(row+n,col,n)
        z_search(row+n,col+n,n)
    else:
        if row == r and col == c:
            print(cnt) 
        elif row==r and col+1==c:
            print(cnt+1)
        elif row+1==r and col==c:
            print(cnt+2)
        else:
            print(cnt+3)
        exit(0)

z_search(0,0,n)


