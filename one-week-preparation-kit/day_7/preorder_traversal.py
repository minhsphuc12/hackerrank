class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""



tree = BinarySearchTree()

# arr = list(map(int, input().split()))
arr = [9,4,6,8,43,2,6,34]

for i in range(len(arr)):
    tree.create(arr[i])

from collections import deque

# def preOrder(root:Node):
#     root = tree.root
#     root.info
#     #Write your code here
#     if root.left is None and root.right is None: 
#         print(root.info)
#     if root.left is not None:
#         print(root.info)
#         return preOrder(root=root.left)
#     if root.left is not None:
#         print(root.info)
#         return preOrder(root=root.right)
    
def preOrder(root:Node):
    if root is None: 
        return
    print(root.info, end=' ')
    preOrder(root.left)
    preOrder(root.right)
    
        

preOrder(tree.root)

tree.root.left.left.info
tree.root.left.right.info
tree.root.right.info