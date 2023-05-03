import sys
nodes = list(map(int, sys.stdin.readline().split()))

class Node:
    def __init__(self,num):
        self.num = num
        self.left = None
        self.right = None

def add_node(parent, node):
    if parent.num < node.num:
        if parent.right:
            add_node(parent.right, node)
        else:
            parent.right = node
    else:
        if parent.left:
            add_node(parent.left, node)
        else:
            parent.left = node 

def print_node(node):
    if node.left:
        print_node(node.left)
    if node.right:
        print_node(node.right)
    print(node.num)


node_list = []
for i in range(len(nodes)):
    if i == 0:
        root = Node(nodes[0])
        node_list.append(root)
    else:
        node = Node(nodes[i])
        node_list.append(node)
        add_node(root, node)

print_node(root)





