from collections import deque
field =[['.','.','.','.','.','.'],
['.','.','.','.','.','.'],
['.','.','.','.','.','.'],
['.','.','.','.','.','.'],
['.','.','.','.','.','.'],
['.','.','.','.','.','.'],
['.','.','.','.','.','.'],
['.','.','.','.','.','.'],
['.','Y','.','.','.','.'],
['.','Y','G','.','.','.'],
['R','R','Y','G','.','.'],
['R','R','Y','G','G','.']]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ans = 0

def bfs(c,x,y):
    queue = deque()
    pop_list = []
    visited =  [[0 for _ in range(6)] for _ in range(12)]
    flag = 0

    queue.append([x,y])
    pop_list.append([x,y])
    visited[x][y] = 1
    
    while queue:
        [x,y] = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < 12 and 0 <= ny < 6 and field[nx][ny] == c and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append([nx,ny])
                pop_list.append([nx,ny])

    if len(pop_list) >= 4:
        flag = 1
        for [x, y] in pop_list:
            field[x][y] = "."

    return flag

def gravity():
    queue = deque()
    for j in range(6):
        for i in range(11,-1,-1):
            if not field[i][j] == '.':
                queue.append(field[i][j])
        for i in range(11,-1,-1):
            if queue:
                q = queue.popleft()
                field[i][j] = q
            else:
                field[i][j] = '.'

while True:
    chk = 0
    for i in range(11,-1,-1):
        for j in range(6):
            if not field[i][j] == '.':
                chk += bfs(field[i][j],i,j)
                
    if chk == 0:
        print(ans)
        break
    else:
        ans += 1
    gravity()
