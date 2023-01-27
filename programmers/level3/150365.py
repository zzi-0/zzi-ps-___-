from collections import deque

def solution(n, m, x, y, r, c, k):
    answer = 'impossible'
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]
    queue = deque()
    queue.append((x-1,y-1,''))

    while len(queue):
        print(queue)
        currentX,currentY,path = queue.popleft()
        if len(path) == k and currentX == r-1 and currentY == c-1:
            answer = path
            break
        if len(path) < k: 
            for i in range(4):
                nx = currentX + dx[i]
                ny = currentY + dy[i]
                if 0 <= nx < n and 0 <= ny < m: 
                    if i == 0: queue.append((nx,ny,path+'d'))
                    if i == 1: queue.append((nx,ny,path+'l'))
                    if i == 2: queue.append((nx,ny,path+'r'))
                    if i == 3: queue.append((nx,ny,path+'u'))

    return answer

print(solution(2,2,1,1,2,2,2))
# print(solution(3,3,1,2,3,3,4))
