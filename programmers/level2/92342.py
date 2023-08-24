ans = 0
answer = []
def solution(n, info):
    global answer
    def dfs(count,i,r_sum,a_sum,tmp):
        global ans, answer
        if i == 11:
            if r_sum > a_sum:
                if ans < r_sum - a_sum:
                    answer = tmp[:]
                    ans = r_sum - a_sum
                if ans == r_sum - a_sum:
            
                    if sum(tmp) < n:
                        tmp[10] = n - sum(tmp)
                    
                    for i in range(10,-1,-1):
                        if answer[i] == tmp[i]:
                            continue
                        if answer[i] < tmp[i]:
                            answer = tmp[:]
                            break
                        if answer[i] > tmp[i]:
                            break
            return

        score = 10 - i

        # 이기는 경우
        if count >= info[i] + 1:
            result = tmp[:]
            result.append(info[i] + 1)
            dfs(count - info[i] - 1,i+1,r_sum+score,a_sum,result)
        
        # 둘다 0인 경우
        if info[i] == 0:
            result = tmp[:]
            result.append(0)
            dfs(count,i+1,r_sum,a_sum,result)
        

        # 지는 경우
        result = tmp[:]
        result.append(0)
        dfs(count,i+1,r_sum,a_sum+score,result)

    dfs(n,0,0,0,[])
    if answer == []:
        answer = [-1]
    return answer

# print(solution(5,[2,1,1,1,0,0,0,0,0,0,0]))

print(solution(10, [8,8,1,2,3,0,0,0,0,0,0]))
print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))




