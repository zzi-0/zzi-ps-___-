def solution(cap, n, deliveries, pickups):
    answer = 0
    current_cap = cap
    
    remain_deliveries = 0
    for i in deliveries:
        remain_deliveries += i
    
    remain_pickups = 0
    for i in pickups:
        remain_pickups += i

    while 1:
        n = len(deliveries)
        temp_current_cap = min(cap,remain_deliveries)
        temp_deliveries = [0 for _ in range(n)]
        for i in range(n-1,-1,-1):
            if temp_current_cap >= deliveries[i]:
                temp_deliveries[i] = deliveries[i]
                temp_current_cap -= deliveries[i]
            else:
                temp_deliveries[i] = temp_current_cap
                temp_current_cap = 0
                break
        
        max_index = 0
        for i in range(n):
            if temp_deliveries[i] != 0:
                max_index = i
            deliveries[i] -= temp_deliveries[i]
            remain_deliveries -= temp_deliveries[i]
            current_cap -= temp_deliveries[i]
        
        for i in range(n-1,-1,-1):
            if current_cap + pickups[i] <= n:
                current_cap += pickups[i]
                remain_pickups -= pickups[i]
                pickups[i] = 0
            else:
                current_cap += n - current_cap
                pickups[i] -= n - current_cap
                remain_pickups -= n - current_cap
            if current_cap == n:
                break

        answer += 2*(max_index+1)

        if remain_deliveries == 0 and remain_pickups == 0:
            break

        for i in range(n-1,-1,-1):
            if deliveries[i] == 0 and pickups[i] == 0:
                deliveries.pop()
                pickups.pop()
            else:
                break
    
    return answer


print(solution(2,7,[1, 0, 2, 0, 1, 0, 2],[0, 2, 0, 1, 0, 2, 0]))