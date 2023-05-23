# 반대 극이면 반대 방향으로 회전, 같은 극이면 회전 안 함


gear = [[1,1,0,0,1,1,1,0],
[1,0,0,0,0,1,0,1],
[0,1,1,1,1,1,1,0],
[0,1,1,0,1,1,1,1]]
k = 4
r = [[2,-1],[2,-1],[2,1],[2,1]]
ans = 0


# 회전하는 주체에서 dfs로 계속 반대 극이면 회전
def rotate_right(i):
    gear[i] = [gear[i][-1]] + gear[i][:-1]

def rotate_left(i):
    gear[i] = gear[i][1:] + [gear[i][0]]


def dfs(i,d):
    check[i] = 1
    # 톱니바퀴의 오른쪽
    if i+1 < 4 and gear[i+1][6] != gear[i][2] and check[i+1] == 0:
        dfs(i+1,-d)
    # 톱니바퀴의 왼쪽
    if i-1 >= 0 and gear[i-1][2] != gear[i][6] and check[i-1] == 0:
        dfs(i-1,-d)

for [i,d] in r:
    check = [0,0,0,0]
    path = [[i-1,d]]
    dfs(i-1,d)
    for [i, d] in path:
        if d == 1:
            rotate_right(i)
        else:
            rotate_left(i)

for i in range(4):
    if gear[i][0] == '0':
        ans += 0
    else:
        ans += 2**i

print(ans)

