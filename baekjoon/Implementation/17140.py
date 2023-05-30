import sys
input = sys.stdin.readline

r, c, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]
count = 0

def rotated(sticker):
    list_of_tuples = zip(*sticker[::-1])
    return [list(elem) for elem in list_of_tuples]

def r_oper(arr):
    temp = [[] for _ in range(len(arr))]
    max = 0
    for i in range(len(arr)):
        a = arr[i]
        dict = {}
        for j in range(len(a)):
            if a[j] == 0:
                continue
            if a[j] in dict:
                dict[a[j]] += 1
            else:
                dict[a[j]] = 1
                
        sorted_dict = sorted(dict.items(), key = lambda item: (-item[1],-item[0]),reverse=True)
        for k, v in sorted_dict:
            temp[i].append(k)
            temp[i].append(v)
        if len(temp[i]) > 100:
            temp[i] = temp[i][:100]
        if len(temp[i]) > max:
            max = len(temp[i])
    
    for i in range(len(temp)):
        if len(temp[i]) < max:
            for j in range(max-len(temp[i])):
                temp[i].append(0)
                
    return temp

def c_oper(arr):
    temp = [[] for _ in range(len(arr))]
    max = 0
    for i in range(len(arr)):
        a = arr[i]
        dict = {}
        for j in range(len(a)):
            if a[j] == 0:
                continue
            if a[j] in dict:
                dict[a[j]] += 1
            else:
                dict[a[j]] = 1
                
        sorted_dict = sorted(dict.items(), key = lambda item: (-item[1],-item[0]),reverse=True)
        for k, v in sorted_dict:
            temp[i].append(k)
            temp[i].append(v)

        if len(temp[i]) > 100:
            temp[i] = temp[i][:100]
        if len(temp[i]) > max:
            max = len(temp[i])
    
    for i in range(len(temp)):
        if len(temp[i]) < max:
            for j in range(max-len(temp[i])):
                temp[i].append(0)
    
    temp2 = [[] for _ in range(max)]
    
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            temp2[j].append(temp[i][j])

    return temp2


while True:
    if count > 100:
        print(-1)
        break 
    if len(arr) >= r and len(arr[0]) >= c:
        if arr[r-1][c-1] == k:
            print(count)
            break
    if len(arr[0]) <= len(arr):
        arr = r_oper(arr)
    else:
        arr = rotated(arr)
        arr = c_oper(arr)
    count += 1