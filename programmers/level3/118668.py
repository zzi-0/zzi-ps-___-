def solution(alp, cop, problems):
  alp_tgt = 0
  cop_tgt = 0
  
  for problem in problems:
    a,c,_,_,_ = problem
    if alp_tgt < a:
      alp_tgt = a
    if cop_tgt < c:
      cop_tgt = c
  
  if alp >= alp_tgt and cop >= cop_tgt:
    return 0
    
  alp_tgt = max(alp_tgt,alp)
  cop_tgt = max(cop_tgt,cop)
  
  problems.append([0,0,1,0,1])
  problems.append([0,0,0,1,1])
  dp = [[100000 for _ in range(cop_tgt+1)] for _ in range(alp_tgt+1)]
  dp[alp][cop] = 0

  for r in range(alp,alp_tgt+1):
    for c in range(cop,cop_tgt+1):
      for alp_req,cop_req,alp_rwd,cop_rwd,cost in problems:
        if alp_req <= r and cop_req <= c:
          nr,nc = r+alp_rwd, c+cop_rwd
          if nr > alp_tgt:
            nr = alp_tgt
          if nc > cop_tgt:
            nc = cop_tgt
          dp[nr][nc] = min(dp[nr][nc],dp[r][c] + cost)
  
  # print(dp)
  return dp[alp_tgt][cop_tgt]

print(solution(10,10,[[10,15,2,1,2],[20,20,3,3,4]]))
print(solution(0,0,[[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]))