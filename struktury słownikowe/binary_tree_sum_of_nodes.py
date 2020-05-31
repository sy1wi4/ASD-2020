'''
Proszę  zaproponować  algorytm,  który  oblicza  sumę  wszystkich  wartości  w  drzewie  binarnym
zdefiniowanym na węzłach typu:

class BNode:
    def __init__( self, value ):
        self.left   = None
        self.right  = None
        self.parent = None
        self.value  = val

Można korzystać wyłącznie ze stałej ilości pamięci (ale wolno zmieniać strukturę drzewa, pod warunkiem,
że po zakończonych obliczeniach drzewo zostanie przywrócone do stanu początkowego.)
'''

# ALGORYTM:
''' 
Każdy node ma dodatkowe pole state, które informuje o tym, gdzie pójdziemy w kolejnym kroku. Defaultowo
w lewo.
Kolejno próbujemy iść: z góry w lewo, następnie w prawo, potem w górę do rodzica.
Powtarzamy dla każdego node'a, aż przejdziemy całe drzewo - warunkiem końca jest trzecie odwiedzenie roota.
'''

class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.parent=None
        self.left=None
        self.right=None
        self.state='l'  # możliwe też 'r' - prawy oraz 'p' - rodzic

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

def Sum(root):
    Sum=0
    curr=root
    i=0
    while  i!=100:

        if curr.state=='l':
            Sum+=curr.key
            curr.state='r'
            if curr.left is not None:
                curr=curr.left

        elif curr.state=='r':
            curr.state='p'
            if curr.right is not None:
                curr=curr.right

        elif curr.state=='p':
            if curr is root:
                # root ma status parent - czyli odwiedzamy go trzeci raz - kończymy
                break
            curr=curr.parent
        i+=1
    return Sum
