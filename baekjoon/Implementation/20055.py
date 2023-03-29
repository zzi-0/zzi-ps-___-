import sys
input = sys.stdin.readline
from collections import deque

n, k = 5, 8
belt = deque([100, 99, 60, 80, 30, 20, 10, 89, 99, 100])
robot = deque([0] * (2*n))
ans = 0

while True:
    ans+=1
    robot.rotate(1)
    belt.rotate(1)
    robot[2*n-1] = 0
            
    for i in range(n-1,-1,-1):
        if i == n-1 and robot[i]:
            robot[i] = 0
        else:
            if robot[i+1] == 0 and belt[i+1] >= 1 and robot[i]:
                robot[i+1] = 1
                robot[i] = 0
                belt[i+1] -= 1

    if belt[0] and robot[0] == 0:
        robot[0] = 1
        belt[0] -= 1

    if belt.count(0) >= k:
        print(ans)
        break
        