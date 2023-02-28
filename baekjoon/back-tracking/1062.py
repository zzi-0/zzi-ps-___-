n, k = 2, 3
words= ['antaxxxxxxxtica','antarctica']
char = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
check = [0] * 26
ans = 0

for i in range(26):
    if char[i] == 'a' or char[i] == 'n' or char[i] == 'c' or char[i] == 't' or char[i] == 'i': 
        check[i] = 1

print(check)

def dfs(idx,level):
    global ans
    if level == k-5:
        count = 0
        for word in words:
            is_know = True
            for c in word:
                if not check[char.index(c)]:
                    is_know = False
                    break
            if is_know:
                count += 1
        if ans < count:
            ans = count
        return

    for i in range(idx,26):
        if check[i] == 0:
            check[i] = 1
            dfs(i,level+1)
            check[i] = 0

if k < 5:
    print(0)
elif k == 26:
    print(n)
else:
    dfs(0,0)
    print(ans)
    
