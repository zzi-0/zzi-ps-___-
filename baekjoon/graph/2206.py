from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(2)]
queue = deque()
queue.append((0,0,1,0))
visited[0][0][0] = 1

dx = [0,1,0,-1]
dy = [1,0,-1,0]

while len(queue):
    x,y,count,crush = queue.popleft()

    if x == n-1 and y == m-1:
        print(count)
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:

            # 만약 부신적이 있다면
            if crush:
                # 변 안부수기만 가능함 
                if graph[nx][ny] == 0 and visited[crush][nx][ny] == 0:
                    visited[crush][nx][ny] = 1
                    queue.append((nx,ny,count+1,crush))
            else:
                # 벽 안부수기 (칸이어야 함 + 방문 X)
                if graph[nx][ny] == 0 and visited[crush][nx][ny] == 0:
                    visited[crush][nx][ny] = 1
                    queue.append((nx,ny,count+1,crush))

                # 벽 부수기 (벽 부순적 없어야 함 + 벽이어야 함 + 방문 한적 없어야 함)
                if visited[1][nx][ny] == 0 and graph[nx][ny] == 1:
                    visited[1][nx][ny] = 1
                    queue.append((nx,ny,count+1,1))

else:print(-1)