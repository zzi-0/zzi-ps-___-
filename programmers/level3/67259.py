from collections import deque

def solution(board):
    queue = deque()
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    n = len(board)
    queue.append((0,0,-1))

    while queue:
        x,y,bd = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 1:
                if bd % 2 == d % 2 or bd == -1:
                    if board[nx][ny] >= board[x][y] + 100 or board[nx][ny] == 0:
                        board[nx][ny] = board[x][y] + 100
                        queue.append((nx,ny,d))
                else:
                    if board[nx][ny] >= board[x][y] + 600 or board[nx][ny] == 0:
                        board[nx][ny] = board[x][y] + 600
                        queue.append((nx,ny,d))


    return board[n-1][n-1]

#print(solution([[0,0,0],[0,0,0],[0,0,0]]))
#print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))