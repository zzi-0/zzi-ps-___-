from collections import deque
import copy

def solution(board):
    answer = min(bfs(board, 1), bfs(board, 2))
    return answer

def bfs(board, start):
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    n = len(board)
    
    queue = deque()
    visited = copy.deepcopy(board)
    queue.append((0,0,0,start))
    
    while queue:
        x,y,c,bd = queue.popleft()
            
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] != 1:
                if bd == d:
                    if visited[nx][ny] > c + 100 or visited[nx][ny] == 0:
                        visited[nx][ny] = c + 100
                        queue.append((nx,ny,c+100,d))
                else:
                    if visited[nx][ny] > c + 600 or visited[nx][ny] == 0:
                        visited[nx][ny] = c+ 600
                        queue.append((nx,ny,c+600,d))
    return visited[-1][-1]