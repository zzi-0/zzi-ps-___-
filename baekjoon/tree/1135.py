import sys

"""
내가 두명의 부하 직원에게 연락하라고 시키면 결과적으로 총 걸리는 시간은 둘 중에 가장 큰 값
"""

def solution():

    input = sys.stdin.readline

	#입력받는 부분
    N = 5
    bose_info = [-1,0,0,2,2]
    #트리로 만들어 준다.
    tree = [[] for _ in range(N)]
    for me, bose in enumerate(bose_info):
        if bose != -1:
            tree[bose].append(me)
	
    #dp[i] : i번째 노드를 루트로 하는 서브트리에 뉴스를 전달하는데 필요한 최대 시간
    dp = [0 for i in range(N)]
    
    def dfs(here):
        temp=[]
       
        for slave in tree[here]:# 내 부하들을 대상으로
            dfs(slave) #leaf 노드까지 내려가준다.
            temp.append(dp[slave]) #부하 놈들이 소식을 전파하는데 걸리는 시간을 담아준다.
        
        if temp: # 만약 부하가 있다면 부하 놈들중 시간이 많이 걸리는 순으로 뉴스를 전달해줘야 전체 시간을 아낄 수 있다. 그래서 정렬 후 이번 단계에서 걸리는 시간을 더해줬다. 
            temp.sort(reverse=True) #시간 정보를 담은 리스트를 정렬 해준다.
            #서브트리에 전파하는 시간 + 이번 단계에서 걸리는 시간(i+1) : 첫번쨰 친구는 1 두번째 친구는 2.. n번째 친구는 n 
            next_time = [temp[i] + i + 1 for i in range(len(temp))] 
            #그중에서 가장 큰 걸 더해준다.
            dp[here] = max(next_time)

    dfs(0)
    print(dp[0])
solution()