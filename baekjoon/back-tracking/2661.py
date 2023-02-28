import sys
from itertools import product

n = int(sys.stdin.readline())

check = []
for i in range(1,4):
    for comb in product([1,2,3], repeat=i):  
        num = "".join(map(str, comb))
        num += num
        check.append(num)


for comb in product([1,2,3], repeat=n):
    comb = list(comb)
    num = "".join(map(str, comb))
    is_good_num = True  
    for c in check:
        if c in num:
            is_good_num = False
            break
    if is_good_num:
        print(num)
        break