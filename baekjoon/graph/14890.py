# dfs, bfs 돌면서 경사로 한 것들 체크하면서 몇개인지 세어보기.

n, l = 6, 2
board = [[3, 2, 1, 1, 2, 3],
[3, 2, 2, 1, 2, 3],
[3, 2, 2, 2, 3, 3],
[3, 3, 3, 3, 3, 3],
[3, 3, 3, 3, 2, 2],
[3, 3, 3, 3, 2, 2]]
ans = 0

def check_line(line):
    slope = [False] * n
    for i in range(n - 1):
        if abs(line[i] - line[i + 1]) > 1:
            return False
        elif line[i] == line[i+1]:
            continue
        # 1 1 2
        elif line[i] < line[i + 1]:
            temp = line[i]
            for j in range(i, i - l, -1):
                if 0 <= j < n:
                    if line[j] != temp:
                        return False
                    if slope[j]:
                        return False
                    slope[j] = True
                else:
                    return False
        # 2 1 1
        elif line[i] > line[i + 1]:
            temp = line[i + 1]
            for j in range(i + 1, i + 1 + l):
                if 0 <= j < n:
                    if line[j] != temp:
                        return False
                    if slope[j]:
                        return False
                    slope[j] = True
                else:
                    return False
    return True



for i in range(n):
    if check_line([board[i][j] for j in range(n)]):
        ans += 1

for j in range(n):
    if check_line([board[i][j] for i in range(n)]):
        ans += 1

print(ans)