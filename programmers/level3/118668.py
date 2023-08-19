def solution(alp, cop, problems):
  max_alp = alp
  max_cop = cop
  
  for [alp_req, cop_req, alp_rwd, cop_rwd, cost] in problems:
    if max_alp < alp_req:
      max_alp = alp_req
    if max_cop < cop_req:
      max_cop = cop_req
  
  if alp >= max_alp and cop >= max_cop:
    return 0
  
  problems.append([0,0,1,0,1])
  problems.append([0,0,0,1,1])

  board = [[10000 for _ in range(max_cop+1)] for _ in range(max_alp+1)]
  board[alp][cop] = 0

  for x in range(alp, max_alp+1):
    for y in range(cop, max_cop+1):
      for [alp_req, cop_req, alp_rwd, cop_rwd, cost] in problems:
        if alp_req <= x and cop_req <= y:
          nx = x + alp_rwd
          ny = y + cop_rwd

          if max_alp < nx:
            nx = max_alp
          if max_cop < ny:
            ny = max_cop
          
          board[nx][ny] = min(board[nx][ny],board[x][y] + cost)
  
  return board[max_alp][max_cop]


  

print(solution(10,10,[[10,15,2,1,2],[20,20,3,3,4]]))
print(solution(0,0,[[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]))