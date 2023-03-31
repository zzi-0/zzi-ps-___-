n = 10
balls = [[1, 10],
[1, 10],
[2, 10],
[3, 10],
[1, 9],
[1, 8],
[1, 7],
[2, 3],
[3, 1],
[3, 1]]

for i in range(n):
    balls[i].append(i)
balls.sort(key = lambda x : (x[1],x[0]))

total_sum = 0
acc_balls = []
color_sum = [0 for _ in range(n+1)]
ans = [0] * n

for i in range(n):
    color, size, index = balls[i]
    sum = total_sum
    for j in range(len(acc_balls)-1,-1,-1):
        a_color,a_size,a_index = acc_balls[j]
        if a_size != size:
            ans[index] = sum - color_sum[color]
            break
        # 사이즈가 같으면 계속 ball 사이즈 빼기
        else:
            if a_color != color:
                sum -= a_size
    # 지금까지의 공 누적
    acc_balls.append(balls[i])
    # color_sum에 color 별로 누적
    color_sum[color] += size
    # total에 총 사이즈 누적
    total_sum += size

for a in ans:
    print(a)
