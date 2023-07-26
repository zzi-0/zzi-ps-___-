def solution(k, n, reqs):
    remains = n - k
    types = [[] for _ in range(k+1)]
    # 각 유형마다 상담원 수 저장
    count = [1 for _ in range(k+1)]


    for [a,b,c] in reqs:
        types[c].append((a,b))

    while True:

        acc = [0] * (k+1)
        for i in range(1,k+1):
            # 각 유형마다 끝나는 시각 저장하기
            times = [0] * count[i]
            for start,end in types[i]:
                is_possible = False
                
                min_time_index = -1
                min_time = 1000000
                for j in range(len(times)):
                    if times[j] <= start:
                        is_possible = True
                    if min_time > times[j]:
                        min_time_index = j
                        min_time = times[j]
                if is_possible:
                    times[min_time_index] = start + end
                else:
                    # 상담 못해서 가장 빠른 시간 알아내기
                    acc[i] += (times[min_time_index] - start)
                    times[min_time_index] += end
        max_time_index = -1
        max_time = 0
        if remains == 0:
            break
        for i in range(1,k+1):
            if max_time < acc[i]:
                max_time_index = i
                max_time = acc[i]
        count[max_time_index] += 1
        remains -= 1
    
        
    return sum(acc)

#print(solution(3,5,[[10, 60, 1], [10, 60, 2], [10,60,3],[10,20,3]]))

