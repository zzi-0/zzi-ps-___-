N = 9
sheet = [1, 2, 3, 3, 4, 1, 10, 8, 1]
Q = 5
nums = [[1, 3],[2, 5],[4, 7],[9, 9],[5, 9]]

N = 6
sheet = [573, 33283, 5572, 346, 906, 567]
Q = 5
nums = [[5, 6],
[1, 3],
[2, 2],
[1, 6],
[3, 6]]

dp = [0 for _ in range(N+1)]
changed = [False for _ in range(N+1)]

for i in range(N):
    if i != N-1 and sheet[i] > sheet[i+1]:
        dp[i+1] = dp[i] + 1
        changed[i+1] = True
    else:
        dp[i+1] = dp[i]


for start_num,end_num in nums:
    ans = dp[end_num] - dp[start_num - 1]
    if changed[end_num]:
        ans -= 1
    print(ans)