import sys
input = sys.stdin.readline

def find(parent, x):
    if x != parent[x]:
        parent[x] = find(parent, parent[x])

    return parent[x]

# 사실을 아는 사람과 Union시, 해당 사람이 부모노드가 되도록
def union(parent, a, b, know_truth):
    a = find(parent, a)
    b = find(parent, b)

    if a in know_truth and b in know_truth:
        return

    if a in know_truth:
        parent[b] = a
    
    elif b in know_truth:
        parent[a] = b
    
    else:
        if a < b:
            parent[b] = a
        
        else:
            parent[a] = b


n, m = map(int, input().split())
know_truth = list(map(int, input().split()))[1:]

parties = []
parent = list(range(n+1))

for _ in range(m):
    party_info = list(map(int, input().split()))
    party_len = party_info[0]
    party = party_info[1:]
    
    for i in range(party_len - 1):
        union(parent, party[i], party[i+1], know_truth)
    
    parties.append(party)
    
ans = 0
for i in range(1,n+1):
    if parent[i] in know_truth and i not in know_truth:
        know_truth.append(i)

for k in parties:
    if all (a not in know_truth for a in k):
        ans += 1

print(ans)