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
        subordinate=[]
       
        for sub in tree[here]: # 내 부하들을 대상으로
            dfs(sub) # leaf 노드까지 내려가준다.
            subordinate.append(dp[sub]) # 부하들이 소식을 전파하는데 걸리는 시간을 담아준다.
        
        if subordinate: # 부하가 있다면 
            subordinate.sort(reverse=True) # 부하들이 소식을 전파하는데 걸리는 시간을 정렬 해준다.

            # 오래 걸리는 부하들부터 전파한다. 
            for i in range(len(subordinate)):
                dp[here] = max(dp[here], subordinate[i] + i + 1)

    dfs(0)
    print(dp[0])
solution()