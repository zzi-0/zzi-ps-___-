def solution(a):
    # 기준값(x)을 기준으로 둘중 한 구간 왼쪽구간(left)이나 오른쪽구간(right)의 최솟값 보다 작으면 됨  
    # -> 왜냐면 항상 마지막에는 기준값의 왼쪽구간과 오른쪽구간에서 최솟값들이 남게 되는데 left_min x right_min x가 최솟값보다 작으면 하나를 제거할 수 있고, 
    # 작은 거 터트리는 거는 한 번 기회가 있기 때문에 나머지 하나도 제거할 수 있기 때문에

    answer = 0
    left_min = [10e9+1] * len(a)
    right_min = [10e9+1] * len(a)

    left_min[0]=a[0]
    for i in range(len(a)):
        left_min[i] = min(left_min[i-1],a[i])
    
    right_min[-1]=a[-1]
    for i in range(len(a)-2,-1,-1):
        right_min[i] = min(right_min[i+1],a[i])

    for i in range(len(a)):
        if left_min[i]>=a[i] or right_min[i]>=a[i]:
            answer+=1
        

    return answer

print(solution([9,-1,-5]))
print(solution([-16,27,65,-2,58,-92,5,-71,-68,-61,-33]))