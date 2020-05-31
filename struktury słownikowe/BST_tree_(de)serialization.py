'''
Podaj algorytm zamieniający drzewo BST w łańcuch odsyłaczowy, w taki sposób, 
aby możliwe było potem odtworzenie tego drzewa z identyczną strukturą. Jest to tak 
zwany problem serializacji drzewa. Znajduje on zastosowanie między innymi w kompresji tekstu.
'''

# ALGORYTM 
'''
PORZĄDEK PRE-ORDER: wypisz root, lewy, prawy
PORZĄDEK IN-ORDER: lewy, wypisz root, prawy
PORZĄDEK POST-ORDER: lewy, prawy, wypisz root

Serializacja: 
    utworzenie listy z wartości w drzewie w porządku preorder: korzeń, lewe poddrzewo, prawe poddrzewo.

Deserializacja: 
    mamy daną listę wartości preorder, z których chcemy zrobić drzewo, pierwsza wartość to korzeń drzewa.
    Wykorzystamy do tego stos, żeby nie robić rekurencyjnie (ale tak też się da).

1.  Utwórz stos.
2.  Pierwsza wartość to root -zrób z niej roota tworzonego drzewa i wrzuć wierzchołek na stos.
3.  Tak długo, jak wartość w liście jest większa niż wartość ze szczytu stosu, usuwaj z wierzchołka stosu. 
    Zrób z danej wartości wierzchołek i zrób z niego prawe dziecko ostatniego usuniętego wierzchołka. Wrzuć nowy wierzchołek na stos.
4.  Jeżeli wartość w liście jest mniejsza niż wartość ze szczytu stosu, zrób z niej lewe dziecko wierzchołka ze szczytu stosu. Wrzuć nowy wierzchołek na stos.
5.Powtarzaj kroki 3 i 4 tak długo, jak jeszcze są rzeczy w liście.

'''
# node w liście
class list_node:
    def __init__(self,node):
        self.node=node  # węzeł drzewa w linked liście
        self.next=None

# dodaj do linked listy węzeł drzewa (na koniec)
def insert_to_list(head,last,tree_node):
    if last is None : 
        head=list_node(tree_node)
        last=head
    else:
        last.next=list_node(tree_node)
        last=last.next
    return last
    
# node w drzewie
class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.parent=None
        self.left=None
        self.right=None

# wstaw do drzewa BST
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

# utwórz listę w porządku pre-order (wpisz,lewy,prawy)
def preorder(root,head,last):
    
    if root is not None:
        last=insert_to_list(head,last,root)
        last=preorder(root.left,head,last)
        last=preorder(root.right,head,last)
    return last

def print_list(head):
    curr=head
    while(curr is not None):
        print(curr.node.key,"-> ",end="")
        curr=curr.next
    print(" None\n")

#######################################################################################
################### WŁAŚCIWY ALGORYTM (DE)SERIALIZACJI DRZEWA #############################
#######################################################################################

# serializacja drzewa - tworzymy listę w porządku inorder
def serialize(root):
    first=list_node(None)
    last=first
    last=preorder(root,first,last)

    return first.next
    

from collections import deque

# deserializacja - odtwarzamy drzewo
def deserialize(first):
    stack=deque()
    curr_node=first
    root=curr_node.node      # korzeń odtwarzanego drzewa
    stack.append(curr_node.node)
    curr_node=curr_node.next

    while curr_node is not None:
        
        if curr_node.node.key>stack[len(stack)-1].key:  # szczyt stosu
            
            while(curr_node is not None and len(stack) != 0 and curr_node.node.key>stack[len(stack)-1].key):
                
                last_popped=stack.pop()
        
            if curr_node is None:
                break
            else:
                last_popped.right=curr_node.node
                stack.append(curr_node.node)
                curr_node=curr_node.next
        else:
            stack[len(stack)-1].left=curr_node.node
            stack.append(curr_node.node)
            curr_node=curr_node.next
    return root
