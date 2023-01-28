def solution(cap, n, deliveries, pickups):
    answer = 0
    
    remain_deliveries = 0
    for i in deliveries:
        remain_deliveries += i
    
    remain_pickups = 0
    for i in pickups:
        remain_pickups += i
        
    while 1:
        current_cap = cap
        delivery_max_index = 0

        for i in range(n):
            delivery_max_index = i
            if current_cap >= deliveries[i]:
                current_cap -= deliveries[i] 
                remain_deliveries -= deliveries[i] 
                deliveries[i] = 0
            else:
                remain_deliveries -= current_cap
                deliveries[i] -= current_cap
                current_cap = 0
            if current_cap == 0:
                break
        
        for i in range(delivery_max_index-1,-1,-1):
            if current_cap + pickups[i] <= n:
                current_cap += pickups[i] 
                remain_pickups -= pickups[i] 
                pickups[i] = 0
            else:
                current_cap += n - pickups[i]
                remain_pickups -= n - pickups[i]
                pickups[i] -= n - pickups[i]
            if current_cap == n:
                break

        answer += 2 * (delivery_max_index + 1)
        if remain_pickups == 0 and remain_deliveries == 0:
            break
    

    return answer


print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2],[0, 2, 0, 1, 0, 2, 0]))