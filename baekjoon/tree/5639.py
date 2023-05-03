import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

nodes = []
while True:
    try:
        nodes.append(int(input()))
    except:
        break

def post_order(start,end):
    if start > end:
        return
    mid = end + 1
    for i in range(start+1, end+1):
        if nodes[i] > nodes[start]:
            mid = i
            break
    
    post_order(start+1,mid-1)
    post_order(mid,end)

    print(nodes[start])


post_order(0, len(nodes) - 1)




