n, k = 10, 32
sequence = [1, 3, 4, 5, 8, 9, 15, 30, 31, 32]

""" n, k = 12, 9
sequence = [3, 5, 6, 8, 9, 10, 13, 15, 16, 22, 23, 25]

n, k = 19, 1000
sequence = [7, 10, 11, 12, 13, 15, 17, 18, 22, 700, 800, 900, 1000, 2000, 4000, 10001, 10002, 10004, 30000] """
""" 1 [3]
3 [5]
4 [7]
5 [10]
8 [23]
9
15
30
31
32 """


graph = [[n] * 0 for _ in range(n)]
j = 0
k_index = 0
ans = 0

for i in range(1, n-1):
    if sequence[i] == k:
        k_index = j
    if sequence[i] == sequence[i+1] - 1:
        graph[j].append(sequence[i])
    else:
        graph[j].append(sequence[i])
        j += 1

if sequence[n-1] == k:
    k_index = j
graph[j].append(sequence[n-1])

for g in graph:
    if sequence[k_index] in g:
        for a in g:
            if a == sequence[k_index]:
                continue
            else:
                ans += len(graph[sequence.index(a)])

print(ans)