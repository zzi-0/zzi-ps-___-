def shift(rc,n,m):
    answer = [[0 for _ in range(m)] for _ in range(n)]

    for j in range(m):
        answer[0][j] = rc[n-1][j]
    for i in range(n-1):
        for j in range(m):
            answer[i+1][j] = rc[i][j]
    
    return answer

def rotate(rc,n,m):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    x,y = 0,1
    i = 0
    before = rc[0][0]
    while True:
        if x == 0 and y == 0:
            before,rc[x][y] = rc[x][y],before 
            break
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            before,rc[x][y] = rc[x][y],before 
            x = nx
            y = ny
        else:
            i += 1
    return rc


def solution(rc, operations):
    answer = rc
    for operation in operations:
        if operation == 'Rotate':
            answer = rotate(answer,len(rc),len(rc[0]))
        if operation == 'ShiftRow':
            answer = shift(answer,len(rc),len(rc[0]))
        print_rc(answer)
    return answer

def print_rc(rc):
    for i in rc:
        print(i)
    print("")

print(solution(	[[8, 6, 3], [3, 3, 7], [8, 4, 9]], ["Rotate", "ShiftRow", "ShiftRow"]))