'''
Dane są dwa drzewa czerwono-czarne reprezentujące zbiory liczb. Proszę zaproponować algorytm obliczający drzewo 
czerwono-czarne będące sumą tych zbiorów.
'''

# ALGORYTM:
'''
Wpisujemy do 2 tablic wartości z obu drzew w porządku in-order, następnie łaczymy te tablice, nie biorąc powtarzających 
się elementów - teraz łatwo możemy utworzyć  drzewo czerwono czarne biorąc za każdym razem medianę tablicy.
Kolorowanie tego drzewa przedstawia się następująco - wszystkie węzły na czarno, a te z ostatniego poziomu
(jedynego, który może być niepełny) na czerwono.
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


def build_balanced_tree(arr):

    if not arr: return
   
    middle=len(arr)//2
    root=Node(arr[middle],1)
        
    root.left=build_balanced_tree(arr[:middle])
    root.right=build_balanced_tree(arr[middle+1:])
    return root

def sum_of_trees(root1,root2):

    # wpisujemy drzewa do tablic w porządku in-order
    def inorder_to_array(root,arr):
        if root is not None:
            inorder_to_array(root.left,arr)
            arr.append(root.key)
            inorder_to_array(root.right,arr)
        return arr

    arr1=[]
    arr1=inorder_to_array(root1,arr1)

    arr2=[]
    arr2=inorder_to_array(root2,arr2)
    res=[None]*(len(arr1)+len(arr2))

    i=j=0
    idx=0

    # łączymy listy bez powtórzeń
    while(i<len(arr1) and j<len(arr2)):
        if arr1[i]==arr2[j]:
            res[idx]=arr1[i]
            i+=1
            j+=1
            idx+=1
        elif arr1[i]<arr2[j]:
            res[idx]=arr1[i]
            i+=1
            idx+=1
        else:
            res[idx]=arr2[j]
            j+=1
            idx+=1
    
    # zostały tylko elementy z 1 tablicy
    while(i<len(arr1)):
        res[idx]=arr1[i]
        idx+=1
        i+=1

    # zostały tylko elementy z 2 tablicy
    while(j<len(arr2)):
        res[idx]=arr2[j]
        idx+=1  
        j+=1 
    
    ctr=0  # liczba niepowtarzających się elementów
    while(ctr!=len(res) and res[ctr] is not None):
        ctr+=1

    res=res[:ctr]

    return build_balanced_tree(res)
