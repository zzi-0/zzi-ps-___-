# dfs, bfs 돌면서 경사로 한 것들 체크하면서 몇개인지 세어보기.

n, l = 6, 2
map = [[3, 2, 1, 1, 2, 3],
[3, 2, 2, 1, 2, 3],
[3, 2, 2, 2, 3, 3],
[3, 3, 3, 3, 3, 3],
[3, 3, 3, 3, 2, 2],
[3, 3, 3, 3, 2, 2]]

""" n, l = 6, 1
map = [[3, 2, 1, 1, 2, 3],
[3, 2, 2, 1, 2, 3],
[3, 2, 2, 2, 3, 3],
[3, 3, 3, 3, 3, 3],
[3, 3, 3, 3, 2, 2],
[3, 3, 3, 3, 2, 2]] """

ans = 0

def go_right(row,col,acc):
    if col == n-1:
        return True
    # 다음 map이 같은 경우
    if map[row][col] == map[row][col+1]:
        return go_right(row,col+1,acc+1)
    # 다음 map이 큰 경우 && acc이 l보다 커야함
    if map[row][col] == map[row][col+1] - 1 and acc >= l:
        return go_right(row,col+1,1)

    # 다음 map이 작은 경우 뒤에 나오는 map들이 다 -1 작아야함
    if col + l < n:
        check = True
        for i in range(1,l+1):
            if map[row][col] != map[row][col+i] + 1:
                check = False
            if not check:
                break
        if check:
            return go_right(row,col+l,1)
    return False

def go_down(row,col,acc):
    if row == n-1:
        return True
    # 다음 map이 같은 경우
    if map[row][col] == map[row+1][col]:
        return go_down(row+1,col,acc+1)
    # 다음 map이 큰 경우 && acc이 l보다 커야함
    if map[row][col] == map[row+1][col] - 1 and acc >= l:
        return go_down(row+1,col,1)

    # 다음 map이 작은 경우 뒤에 나오는 map들이 다 -1 작아야함
    if row + l < n:
        check = True
        for i in range(1,l+1):
            if map[row][col] != map[row+i][col] + 1:
                check = False
            if not check:
                break
        if check:
            return go_down(row+l,col,1)
    return False
        

for i in range(n):
    if go_right(i,0,1):
        ans += 1
    if go_down(0,i,1):
        ans += 1

print(ans)



