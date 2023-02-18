import sys

def input():
    return sys.stdin.readline().rstrip()

def solution(n, k):
    answer = 'YES'
    lt = 0
    rt = n / 2

    while (lt <= rt):
        mid = (lt + rt) / 2
        rowCount = mid
        columnCount = n - mid

        count = (rowCount + 1) * (columnCount + 1)

        if count == k:
            return answer
        
        elif count > k:
            rt = mid - 1
        else:
            lt = mid + 1
        
    answer = 'NO'
    return answer

arr = input().split(" ")
print(solution(int(arr[0]),int(arr[1])))

