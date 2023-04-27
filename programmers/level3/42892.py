import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, x, y, id):
        self.x = x
        self.y = y
        self.id = id
        self.left = None
        self.right = None

def addNode(parent, child):
    if parent.x < child.x:
        if parent.right == None:
            parent.right = child
        else:
            addNode(parent.right, child)
    else:
        if parent.left == None:
            parent.left = child
        else:
            addNode(parent.left, child)

def preorder(v,result):
    result.append(v.id)
    if v.left:
        preorder(v.left,result)
    if v.right:
        preorder(v.right,result)
    return result
    
def postorder(v, result):
    if v.left:
        postorder(v.left,result)
    if v.right:
        postorder(v.right,result)
    result.append(v.id)
    return result

def solution(nodeinfo):
    answer = [[],[]]
    nodelist = []

    for i in range(len(nodeinfo)):
        x,y = nodeinfo[i]
        nodelist.append(Node(x,y,i+1))

    nodelist.sort(key = lambda object : (object.y,-object.x), reverse=True)

    root = nodelist[0]

    for i in range(1,len(nodelist)):
        node = nodelist[i]
        addNode(root,node)

    answer[0] = preorder(root,[])
    answer[1] = postorder(root,[])

    return answer

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))
