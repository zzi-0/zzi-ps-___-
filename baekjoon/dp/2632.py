import sys
from collections import defaultdict
def input(): return sys.stdin.readline().rstrip()

def find_case(pizza, length):
    case = defaultdict(int)
    for p1 in range(length):
        stack = []
        for p2 in range(length):
            p = (p1 + p2) % length
            stack.append(pizza[p])
            case[sum(stack)] += 1
    case[sum(pizza)] = 1 
    return case

k = int(input())
n, m = map(int,input().split())
pizza_a = [int(input()) for _ in range(n)]
pizza_b = [int(input()) for _ in range(m)]

case1 = find_case(pizza_a, n)
case2 = find_case(pizza_b, m)

result = case1.get(k, 0) + case2.get(k, 0)
for num in case1:
    if k-num in case2:
        result += case1[num] * case2[k-num]

print(result)
