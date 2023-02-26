from sys import stdin

def dfs(player_count,sum):
    global ans
    if player_count == 11:
        if ans < sum:
            ans = sum
        return
    for i in range(11):
        if visited[i] == 0 and arr[player_count][i] != 0:
            visited[i] = 1
            dfs(player_count + 1, sum + arr[player_count][i])
            visited[i] = 0

T = int(stdin.readline())
for tc in range(T):
    arr =[]
    for _ in range(11):
        arr.append(list(map(int,stdin.readline().split())))
    visited =[0]*11
    ans = 0
    dfs(0,0)
    print(ans)


