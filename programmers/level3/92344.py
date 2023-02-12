def solution(board, skill):
    answer = 0
    n = len(board)
    m = len(board[0])
    d = [[0]*1003 for _ in range(1003)]

    for [type, startRow, startCol, endRow, endCol, degree ] in skill:
        if type == 1: 
            degree = -degree
        d[startRow][startCol] += degree
        d[startRow][endCol+1] -= degree
        d[endRow+1][startCol] -= degree
        d[endRow+1][endCol+1] += degree

    for i in range(1,n):
        for j in range(m):
            d[i][j] += d[i-1][j]
    
    for i in range(n):
        for j in range(1,m):
            d[i][j] += d[i][j-1]
    
    for i in range(n):
        for j in range(m):
            if board[i][j] + d[i][j] > 0:
                answer+=1

    return answer


print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]]))
