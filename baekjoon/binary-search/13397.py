n, m = 8, 3
arr = [1, 5, 4, 6, 2, 1, 3, 100]
lt = 0
rt = max(arr)
ans = rt


def isVaild(value):
    global m
    min = arr[0]
    max = arr[0]
    section = 1

    for num in arr:
        if num < min:
            min = num
        if num > max:
            max = num
        if max - min > value:
            max = num
            min = num
            section += 1
    
    return section <= m



while lt <= rt:
    mid = (lt+rt) // 2
    if isVaild(mid):
        rt = mid - 1
        ans = mid
    else:
        lt = mid + 1

print(ans)