import sys

input = sys.stdin.readline

n, m = map(int, input().split())
party_hall = [list(map(int, input().split())) for _ in range(n)]
party = [list(map(int, input().split())) for _ in range(m)]


for k in range(n):  
    for i in range(n):  
        for j in range(n): 
            if party_hall[i][j] > party_hall[i][k] + party_hall[k][j]:
                party_hall[i][j] = party_hall[i][k] + party_hall[k][j]

for p in party:
    start, end, cost = p
    if party_hall[start -1][end -1] <= cost:
        print("Enjoy other party")
    else:
        print("Stay here")

