'''
Mając działającą w O(1) funkcję randInt(k) zwracającą losowy int z zakresu [0, k), podaj jak należy 
zmodyfikować drzewo RB, żeby dało się w O(log(n)) pobrać losowy element tego drzewa? Czy zadanie się 
upraszcza, jeśli wolno nam korzystać z tablicy dynamicznej?
'''

# ALGORYTM:
'''
Dla każdego node'a trzymamy także rozmiar prawego i lewego poddrzewa, dzięki czemu łatwo
możemy znaleźć k-ty element w czasie O(logn), ponieważ wyskość drzewa RB nie przekracza logn, a na każdym poziomie
idziemy albo do prawego syna, więc mamy pewność, że nie wykonamy więcej  niż logn operacji.
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
            
