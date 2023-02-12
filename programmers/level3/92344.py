def solution(board, skill):
    answer = 0

    for [type, startRow, startCol, endRow, endCol, degree ] in skill:
        for i in range(startRow,endRow+1):
            for j in range(startCol,endCol+1):
                if type == 1:
                    board[i][j] -= degree
                if type == 2:
                    board[i][j] += degree
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] > 0:
                answer+=1

    return answer


print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]]))
