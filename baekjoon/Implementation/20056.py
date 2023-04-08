n, m, k = 4, 2, 2
fireballs = [[1, 1, 5, 2, 2],
[1, 4, 7, 1, 6]]

""" n, m, k = map(int, input().split())
fireballs = []
for _ in range(m):
    _r, _c, _m, _s, _d = list(map(int, input().split()))
    fireballs.append([_r-1, _c-1, _m, _s, _d]) """

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

board = [[[] for _ in range(n)] for _ in range(n)]

for i in range(k):
    while fireballs:
        # 모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동한다
        [r, c, m, s, d] = fireballs.pop()
        nr = (r + dx[d] * s) % n
        nc = (c + dy[d] * s) % n
        board[nr][nc].append([m,s,d])

    for row in range(n):
        for col in range(n):
            if len(board[row][col]) >= 2:
                sum_m, sum_s, cnt_odd, cnt_even, cnt = 0, 0, 0, 0, len(board[row][col])
                while board[row][col]:
                    _m, _s, _d = board[row][col].pop(0)
                    sum_m += _m
                    sum_s += _s
                    if _d % 2:
                        cnt_odd += 1
                    else:
                        cnt_even += 1
                if cnt_odd == cnt or cnt_even == cnt:  # 모두 홀수이거나 모두 짝수인 경우
                    nd = [0, 2, 4, 6]
                else:
                    nd = [1, 3, 5, 7]
                if sum_m//5:  # 질량 0이면 소멸
                    for d in nd:
                        fireballs.append([r, c, sum_m//5, sum_s//cnt, d])
            if len(board[row][col]) == 1:
                fireballs.append([row, col] + board[row][col].pop())

print(sum([f[2] for f in fireballs]))




