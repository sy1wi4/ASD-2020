# każda operacja ma złożoność O(wysokość drzewa), co przy losowym rozkładzie sprowadza się do O(logn)

# !!! złożoność może w skrajnym przypadku stać się liniowa, jeżeli drzewo stanie się zwykłą listą odsyłaczową

class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.parent=None
        self.left=None
        self.right=None


def find(root,key):
    while root is not None :
        if root.key==key :
            return root
        elif key > root.key :
            root=root.right
        else:
            root=root.left 
    return None


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


def remove(root,key):

    to_remove=find(root,key)
    
    if to_remove is None: return 
    
    elif to_remove.right is None :
        
        # usuwamy liść
        if to_remove.left is None :

            # liść jest lewym dzieckiem
            if to_remove.parent.left is not None and to_remove.parent.left.key==key:
                to_remove.parent.left=None

            # liść jest prawym dzieckiem
            else:
                to_remove.parent.right=None

        else:
            # usuwany ma tylko lewe dziecko
            # sprawdzam czy usuwany był prawym czy lewym dzieckiem rodzica, aby przepiąć jego dzieci

            if to_remove.parent.left is not None and to_remove.parent.left.key==to_remove.key :
                to_remove.parent.left=to_remove.left
        
            elif to_remove.parent.right is not None and to_remove.parent.right.key==to_remove.key :
                to_remove.parent.right=to_remove.left

    elif to_remove.left is None :
        # usuwany ma tylko prawe dziecko
        # sprawdzam czy usuwany był prawym czy lewym dzieckiem rodzica, aby przepiąć jego dzieci
        if to_remove.parent.left is not None and to_remove.parent.left.key==to_remove.key :
            to_remove.parent.left=to_remove.right
        
        elif to_remove.parent.right is not None and to_remove.parent.right.key==to_remove.key :
            to_remove.parent.right=to_remove.right

    else:  
        # usuwany ma 2 dzieci - szukam poprzednika, jego wartości przepisuję
        # na usuwanego, z oryginalnego miejsca usuwam poprzednika
        succ=successor(root,key)
        Key=succ.key
        Value=succ.value
        remove(root,succ.key)
        to_remove.key=Key
        to_remove.value=Value

        

# następnik 
def successor(root,key):
    node=find(root,key)

    if node is None: return None
    
    # brak prawego poddrzewa
    elif node.right is None:
        if node.parent is None: return None

        # odwrotność operacji poprzednika - dopóki jest prawym synem idę w górę, 
        # następnie 1 w lewo, a jeżeli jest lewym synem, to rodzic

        if node.parent.right is None or (node.parent.right.key != key):
            return node.parent

        else:
            while (node.parent is not None and node.parent.right is not None and node.parent.right.key == node.key):
                node=node.parent
            
            # na koniec jeden krok "w prawo", chyba, że dojdziemy do roota - tzn, że szukamy
            # następnika maxa
            if node.parent is not None : return node.parent
            else: return None
    
    # min z prawego poddrzewa
    else:
        node=node.right

        prev=node.parent
        while(node is not None):
            prev=node
            node=node.left
        return prev


# poprzednik
def predecessor(root,key):
    node=find(root,key)

    if node is None: return None

    # brak lewego poddrzewa
    elif node.left is None:

        if node.parent is None: return None

        # odwrotność operacji następnika - dopóki jest lewym synem idę w górę, 
        # następnie 1 w prawo, a jeżeli jest prawym synem, to rodzic

        if node.parent.left is None or (node.parent.left.key != key):
            return node.parent

        else:
            while (node.parent is not None and node.parent.left is not None and node.parent.left.key == node.key):
                node=node.parent
            
            # na koniec jeden krok "w prawo", chyba, że dojdziemy do roota - tzn, że szukamy
            # poprzednika mina
            if node.parent is not None : return node.parent
            else: return None

    # max z lewego poddrzewa
    else:
        node=node.left
        prev=node.parent
        while(node is not None):
            prev=node
            node=node.right
        return prev



def get_min(root):
    prev=None
    while root is not None:
        prev=root
        root=root.left
    return prev.key

def get_max(root):
    prev=None
    while root is not None:
        prev=root
        root=root.right
    return prev.key
