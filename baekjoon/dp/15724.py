N,M = 4,4
board = [[9, 14, 29, 7],
[1, 31, 6, 13],
[21, 26, 40, 16],
[8, 38, 11, 23]]
K = 3
area_list = [[1, 1, 3, 2],
[1, 1, 1, 4],
[1, 1, 4, 4]]

acu = [[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(N+1):
    for j in range(M):
        if i != 0:
            acu[i][j+1] = acu[i][j] + board[i-1][j]


for i in range(N):
    for j in range(M+1):
        acu[i+1][j] += acu[i][j]

for x1,y1,x2,y2 in area_list:
    print(acu[x2][y2] - acu[x2][y1-1] - acu[x1-1][y2] + acu[x1-1][y1-1])
