'''
Proszę  opisać  jak  zmodyfikować  drzewa  czerwono-czarne (przechowujące liczby jako klucze) 
tak, by operacja sum(T, x, y) obliczająca sumę elementów z drzewa T o wartościach z przedziału [x, y] 
działała w czasie O(logn) (gdzie n to liczba węzłów drzewa T). Pozostał eoperacje na powstałym drzewie 
powinny miec taka sama złożoność jak w standardowym drzewie czerwono-czarnym.
'''

# ALGORYTM
''' 
Dokonujemy następującej modyfikacji - przechowujemy dla każdego węzła sumę lewego i prawego poddrzewa.
Znajdujemy wspólnego roota - ostatni element, po którym ścieżki przy szukaniu x i y się rozdzielają,
następnie póki w drzewie mogą być węzły znajdujące się w zadanym przedziale schodzimy w lewo
lub prawo, w zależności od wartości.
Ta modyfikacja nie zaburzy złożoności pozostałych operacji w drzewie czerwono czarnym, ponieważ
sumy obliczamy już przy wstawianiu, jedyne co musimy zrobić, to przy rotacjach odpowiednio aktalizować sumy,
ale to tyczy się tylko stałej ilości węzłów.
'''


from BST_tree_display import display_tree


class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.parent=None
        self.left=None
        self.right=None
        self.right_sum=0
        self.left_sum=0

# przy wstawianiu aktualizuję lewą i prawą sumę node'ów po drodze
def insert(root,key,value):
    prev=None
    while root is not None :
        if key > root.key :
            root.right_sum+=key
            prev=root
            root=root.right
        else:
            root.left_sum+=key
            prev=root
            root=root.left

    if key < prev.key :
        prev.left=Node(key,value)
        prev.left.parent=prev
    else:
        prev.right=Node(key,value)
        prev.right.parent=prev


def sum_between(root,x,y):

    # szukamy węzła, gdzie ścieżki się rozdzielają
    def common_root(root,x,y):
        while root is not None:
            if root.key>=x and root.key<=y : 
                return root
            elif root.key>y:
                root=root.left
            else:
                root=root.right

    def sum(root,x,y):
        Sum=root.key

        # lewe poddrzewo wspólnego roota
        current=root.left
        while current is not None:
            if current.key>x :
                Sum+=current.right_sum+current.key
                current=current.left
            elif current.key<x:
                current=current.right
            else:
                # kraniec przedziału
                Sum+=current.right_sum+current.key
                break
        
        # prawe poddrzewo
        current=root.right
        while current is not None:
            if current.key<y :
                Sum+=current.left_sum+current.key
                current=current.right
            elif current.key>y:
                current=current.left
            else:
                # kraniec przedziału
                Sum+=current.left_sum+current.key
                break

        return Sum

    Root=common_root(root,x,y)
    return sum(Root,x,y)
