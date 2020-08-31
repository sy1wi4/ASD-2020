'''
Dostajemy dany klucz i mamy znaleźć jego podłogę oraz sufit. 
Jeżeli klucz znajduje się w drzewie, to są one równe kluczowi,
natomiast jeżeli nie, to podłogą jest największy z kluczy mniejszych
od niego, analogicznie z sufitem.
'''

# ALGORYTM:
'''
Szukamy w drzewie elementu o danym kluczu, na bieżąco aktualizując sufit idąc w lewo
oraz podłogę idąc w prawo.
'''

class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.parent = None
        self.left = None
        self.right = None

def insert(root,key,value):
    prev = None
    while root is not None :
        if key > root.key :
            prev = root
            root = root.right
        else:
            prev = root
            root = root.left

    if key < prev.key :
        prev.left = Node(key,value)
        prev.left.parent = prev
    else:
        prev.right = Node(key,value)
        prev.right.parent = prev



def find(root,key):

    ceil = None
    floor = None

    while root is not None :
        if root.key == key :
            return key,key
        elif key > root.key :
            ceil = root.key
            root = root.right
           
        else:
            floor = root.key
            root = root.left 

    return ceil,floor



root=Node(20,1)
insert(root,15,1)
insert(root,25,1)
insert(root,23,1)
insert(root,66,1)
insert(root,10,1)
insert(root,9,1)

print(find(root,19))
