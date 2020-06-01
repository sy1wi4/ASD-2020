'''
Zaimplementować funkcję, która oblicza średnią wartość w drzewie BST.
'''

from BST_tree_display import display_tree

class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.parent=None
        self.left=None
        self.right=None

def insert(root,key,value):
    prev=None
    while root is not None :
        if key > root.key :
            prev=root
            root=root.right
        else:
            prev=root
            root=root.left

    if key < prev.key :
        prev.left=Node(key,value)
        prev.left.parent=prev
    else:
        prev.right=Node(key,value)
        prev.right.parent=prev

Sum=0
ctr=0

def inorder(root):
    global Sum      # suma elementów
    global ctr      # licznik elementów
    if root is not None:
        inorder(root.left)
        Sum+=root.key
        ctr+=1
        inorder(root.right)
    return Sum,ctr

def average(root):
    Sum,ctr=inorder(root)
    return Sum/ctr

root=Node(70,1)
insert(root,15,1)
insert(root,25,1)
insert(root,12,1)
insert(root,58,1)
