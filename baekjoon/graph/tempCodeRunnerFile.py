for [[ax,ay],[bx,by],[cx,cy]] in combinations:
    map[ax][ay] = 1
    map[bx][by] = 1
    map[cx][cy] = 1
    count = bfs(map)
    if count < ans:
        ans = count
    map[ax][ay] = 0
    map[bx][by] = 0
    map[cx][cy] = 0
