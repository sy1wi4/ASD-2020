'''
Podaj algorytm, który mając na wejściu niezrównoważone drzewo BST przekształca 
je w drzewa dające się pokolorować jako czerwono-czarne.
'''

# ALGORYTM
'''
rekurencyjnie wpisujemy do tablicy wartości inorder O(n), następnie z posortowanej 
tablicy łatwo możemy zrobić zbalansowane drzewo, biorąc jako roota medianę.
Drzewo, które otrzymamy jest idealnie zrównoważone, dzięki temu na pewno jest czerwono-czarne.
'''


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



def func(root):

    arr=[]

    # dostajemy klucze z drzewa (niezbalansowanego) w porządku posortowanym
    def inorder_to_array(root,arr):
        if root is not None:
            inorder_to_array(root.left,arr)
            arr.append(root.key)
            inorder_to_array(root.right,arr)
        return arr

    array=inorder_to_array(root,arr)
    print(array)

    # za każdym razem jako roota danego poddrzewa wybieramy środkową wartość z tablicy
    def build_balanced_tree(arr):

        if not arr: return
       
        middle=len(arr)//2
        root=Node(arr[middle],1)
        
        root.left=build_balanced_tree(arr[:middle])
        root.right=build_balanced_tree(arr[middle+1:])
        return root

    return build_balanced_tree(array)
