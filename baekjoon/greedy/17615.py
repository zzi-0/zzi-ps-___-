# 11:35
n = 8
balls = 'RRRRRBBR'
cnt = []

# 우측으로 레드 모으기
rexplore = balls.rstrip('R')
cnt.append(rexplore.count('R'))

# 우측으로 블루 모으기
rexplore = balls.rstrip('B')
cnt.append(rexplore.count('B'))

# 좌측으로 레드 모으기
lexplore = balls.lstrip('R')
cnt.append(lexplore.count('R'))

# 좌측으로 블루 모으기
lexplore = balls.lstrip('B')
cnt.append(lexplore.count('B'))

print(min(cnt))


