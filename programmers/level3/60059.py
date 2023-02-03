# -*- coding: utf-8 -*- 
def attach(x,y,board,key,M):
    for i in range(M):
        for j in range(M):
            board[x+i][y+j] += key[i][j]

def detach(x,y,board,key,M):
    for i in range(M):
        for j in range(M):
            board[x+i][y+j] -= key[i][j]

def check(board,M,N):
    for i in range(N):
        for j in range(N):
            if board[M+i][M+j] != 1:
                return False
    return True

def rotate90(arr):
    return list(zip(*arr[::-1]))

def solution(key, lock):
    M, N = len(key), len(lock)

    board = [[0] * (M*2 + N) for _ in range(M*2 + N)]

    # 자물쇠 중앙 배치
    for i in range(N):
        for j in range(N):
            board[M+i][M+j] = lock[i][j]

    rotated_key = key
    # 모든 방향 (4번 루프)
    for _ in range(4):
        rotated_key = rotate90(rotated_key)
        for x in range(0, M+N):
            for y in range(0, M+N):
                # x+키 길이 만큼, y+키 길이만큼
                attach(x,y,board,rotated_key,M)
                if check(board,M,N):
                    return True
                detach(x,y,board,rotated_key,M)

    return False

print(solution([[1, 1, 0], [1, 1, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))