def solution(cap, n, deliveries, pickups):

    deliveries = deliveries[::-1]
    answer = 0
    d = 0
    
    for i in range(n):
        print(d,answer)
        d += deliveries[i]
        
        while d > 0:
            d -= cap
            answer += (n - i) * 2
    return answer

print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2],[0, 2, 0, 1, 0, 2, 0]))