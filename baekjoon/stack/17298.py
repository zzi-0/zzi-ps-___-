
# -5 7 7 -1
# 뒤에 숫자가 앞에 숫자보다 작은 경우
# 뒤에 숫자가 앞에 숫자보다 큰 경우
n = 4
number = [3, 5, 2, 7]
ans = [-1] * n
stack = []

stack.append(0)
for i in range(1, n):
    while len(stack):
        if number[stack[-1]] < number[i]:
            ans[stack.pop()] = number[i]
        else:
            break
    stack.append(i)

print(ans)