n = 2
words = ['abc','acba']
arr = []

def dfs(check,char_list):
    global arr,result
    if len(arr) == len(char_list):
        print(''.join(arr))
        return
    for i in check:
        if check[i]:
            check[i] -= 1
            arr.append(i)
            dfs(check,char_list)
            check[i] += 1
            arr.pop()

for word in words:
    char_list = list(word)
    char_list.sort()
    arr = []
    check = {}
    for c in char_list:
        if c in check:
            check[c] += 1
        else:
            check[c] = 1
    dfs(check,char_list)
