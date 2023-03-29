import sys
input = sys.stdin.readline

n, k = map(int,input().split())
belt = list(map(int, input().split()))
robot = [0] * (2*n)
ans = 0

def is_stop(belt,k):
    count = 0
    for i in range(len(belt)):
        if belt[i] == 0:
            count += 1
        if count >= k:
            return True
    return False

while True:
    ans+=1
    rotated_robot = [0]*(2*n)
    rotated_belt = [0]*(2*n)
    for i in range(2*n):
        if i == 0:
            rotated_robot[i] = 0
            rotated_belt[i] = belt[2*n-1]
        else:
            rotated_robot[i] = robot[i-1]
            rotated_belt[i] = belt[i-1]
            
    for i in range(n-1,-1,-1):
        if i == n-1 and rotated_robot[i]:
            rotated_robot[i] = 0
        else:
            if rotated_robot[i+1] == 0 and rotated_belt[i+1] >= 1 and rotated_robot[i]:
                rotated_robot[i+1] = 1
                rotated_robot[i] = 0
                rotated_belt[i+1] -= 1

    if rotated_belt[0] and rotated_robot[0] == 0:
        rotated_robot[0] = 1
        rotated_belt[0] -= 1

    if is_stop(rotated_belt,k):
        print(ans)
        break
        
    robot = rotated_robot[:]
    belt = rotated_belt[:]