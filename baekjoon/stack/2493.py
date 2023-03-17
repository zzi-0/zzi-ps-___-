n = 5
tower = [6, 9, 5, 7, 4]
ans = []
stack = []

for i in range(n):
    while len(stack):
        if tower[stack[-1]] >= tower[i]:
            ans.append(stack[-1] + 1)
            break
        else:
            stack.pop()
    else:
        ans.append(0)
    stack.append(i)


print(ans)