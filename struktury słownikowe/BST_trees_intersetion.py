'''
Operacja intersection otrzymuje na wejściu dwa zbiory zrealizowane jako tablice asocjacyjne 
i zwraca ich liczbę elementów, które występują w obu. Proszę zaimplementować tę operację dla 
tablic asocjacyjnych realizowanych jako:
1.  drzewa BST
'''

# ALGORYTM:
'''
Przechodzimy in-order oba drzewa, dostajemy 2 posortowane tablice, następnie liczymy powtarzające się elementy.
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

       

def inorder(root,arr):
    if root is not None:
        inorder(root.left,arr)
        arr.append(root.key)
        inorder(root.right,arr)

def intersection(root1,root2):
    arr1=[]
    arr2=[]
    inorder(root1,arr1)
    inorder(root2,arr2)
    print(arr1)
    print(arr2)

    # szukamy części wspólnych obu tablic
    i=j=0
    common=0  # liczba wspólnych elementów

    while(i<len(arr1) and j<len(arr2)):
        if arr1[i]==arr2[j]:
            common+=1
            i+=1
            j+=1
        elif arr1[i]<arr2[j]:
            i+=1
        else:
            j+=1
            
    return common
