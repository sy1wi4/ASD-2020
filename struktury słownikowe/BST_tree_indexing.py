'''
Rozważmy drzewa BST, które dodatkowo w każdym węźle  zawierają  pole  z  liczbą  węzłów  w  danym  poddrzewie. 
Proszę  opisać  jak  w  takim  drzewie  wykonywaćnastępujące operacje:
1.  znalezienie i-go co do wielkości elementu,
2.  wyznaczenie, którym co do wielkości w drzewie jest zadany węzeł
'''

class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.parent=None
        self.left=None
        self.right=None
        self.right_size=0
        self.left_size=0

# przy wstawianiu aktualizuję rozmiar prawego i lewego poddrzewa
def insert(root,key,value):
    prev=None
    while root is not None :
        if key > root.key :
            root.right_size+=1
            prev=root
            root=root.right
        else:
            root.left_size+=1
            prev=root
            root=root.left

    if key < prev.key :
        prev.left=Node(key,value)
        prev.left.parent=prev
    else:
        prev.right=Node(key,value)
        prev.right.parent=prev

def find(root,key):
    while root is not None :
        if root.key==key :
            return root
        elif key > root.key :
            root=root.right
        else:
            root=root.left 
    return None

#####################################################################################################
#####################################################################################################

# k-ty element
def find_kth(root,k):
    while(root is not None):
        if k == root.left_size+1 :
            return root
        elif k <= root.left_size:
        # szukamy w lewym poddrzewie
            root=root.left
        else:
        # szukamy w prawym poddrzewie
            k-=root.left_size+1
            root=root.right
    return None

# który co do wielkości
def get_index(root,key):
    node=find(root,key)
    idx=1

    # wszystko co w lewym poddrzewie, jest mniejsze
    idx+=node.left_size

    # jeśli jestem lewym synem, to idę dalej, a jeśli prawym to dodaję rozmiar lewego rodzica+1
    while(node.parent is not None):
        if node.parent.right is not None and node.parent.right.key==node.key:
            idx += node.parent.left_size+1
        node=node.parent
    
    return idx
