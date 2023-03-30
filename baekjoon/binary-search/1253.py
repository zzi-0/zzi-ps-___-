n = 3
numbers = [0, 0, 0]
ans = 0
numbers.sort()


for i in range(n):
    tmp = numbers[:i] + numbers[i+1:]
    lt = 0
    rt = len(tmp)-1
    while lt < rt:
        sum = tmp[lt] + tmp[rt]
        if sum == numbers[i]:
            ans += 1
            break
        elif sum > numbers[i]:
            rt -= 1
        else:
            lt += 1

print(ans)

