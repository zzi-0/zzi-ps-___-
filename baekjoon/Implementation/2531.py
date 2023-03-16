n, d, k, c = 8, 30, 4, 30
sushi = [7, 9, 7, 30, 2, 7, 9, 25]
ans = 0

for i in range(k-1):
    sushi.append(sushi[i])

for i in range(n):
    set_sushi = set(sushi[i:i+k])
    set_sushi.add(c)
    if ans < len(set_sushi):
        ans = len(set_sushi)

print(ans)
