import sys

input = sys.stdin.readline

n = int(input())
cranes = list(map(int, sys.stdin.readline().split()))
m = int(input())
boxes = list(map(int, sys.stdin.readline().split()))

ans = 0

cranes.sort()
cranes.reverse()
boxes.sort()
boxes.reverse()
remains_boxes = boxes[:]
next_boxes = []

if boxes[0] > cranes[0]:
    print(-1)
else:

    while len(remains_boxes):
        boxex_idx = 0
        cranes_idx = 0
        while True:
            if remains_boxes[boxex_idx] <= cranes[cranes_idx]:
                boxex_idx += 1
                cranes_idx += 1
            else:
                next_boxes.append(remains_boxes[boxex_idx])
                boxex_idx += 1
            if boxex_idx == len(remains_boxes):
                break
            if cranes_idx == n:
                for i in range(boxex_idx,len(remains_boxes)):
                    next_boxes.append(remains_boxes[i])
                break

        remains_boxes = next_boxes[:]
        next_boxes = []
        ans += 1

    print(ans)
