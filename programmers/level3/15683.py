from itertools import product
from collections import deque
import copy

n, m = 6, 6
office = [[0, 0, 0, 0, 0, 0],
[0, 2, 0, 0, 0, 0],
[0, 0, 0, 0, 6, 0],
[0, 6, 0, 0, 2, 0],
[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 5]]


cctv_count = 0
empty_count = 0
cctv = []
queue = deque()
ans = 0

for i in range(n):
    for j in range(m):
        if 0 < office[i][j] < 6:
            cctv.append([i,j,office[i][j]])
            cctv_count += 1
        if office[i][j] == 0:
            empty_count += 1
ans = empty_count

def watch():
    global queue,ans
    copy_office = copy.deepcopy(office)
    count = 0
    while len(queue):
        x,y,cctv,dir = queue.popleft()
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        d_list = []

        if cctv == 1:
            d_list.append((dir))
        if cctv == 2:
            d_list.append((dir))
            dir = (dir + 2) % 4
            d_list.append((dir))
        if cctv == 3:
            d_list.append((dir))
            dir = (dir + 1) % 4
            d_list.append((dir))
        if cctv == 4:
            d_list.append((dir))
            dir = (dir + 1) % 4
            d_list.append((dir))
            dir = (dir + 2) % 4
            d_list.append((dir))
        if cctv == 5:
            d_list.append((0))
            d_list.append((1))
            d_list.append((2))
            d_list.append((3))

        i_x = x
        i_y = y

        for d in d_list:
            x = i_x
            y = i_y
            while True:
                nx = dx[d] + x
                ny = dy[d] + y
                if 0 <= nx < n and 0 <= ny < m and not copy_office[nx][ny] == 6:
                    if copy_office[nx][ny] == 0:
                        copy_office[nx][ny] = '#'
                        count += 1
                    x = nx
                    y = ny
                else:
                    break
    
    if ans > empty_count-count:
        ans = empty_count-count




for dir in product(range(4),repeat=cctv_count):
    queue = deque()
    for i in range(cctv_count):
        queue.append((cctv[i][0],cctv[i][1],cctv[i][2],dir[i]))
    watch()

print(ans)
