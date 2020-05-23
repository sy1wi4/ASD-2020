'''
Opisz, jak zmodyfikować drzewa czerwono czarne tak, aby można było w czasie O(log(n)) wyznaczyć sumę wszystkich 
elementów w drzewie o wartościach z zakresu (x, y). W wyniku wykonanej modyfikacji pozostałe operacje na drzewie 
również powinny zachować swoją pierwotną złożoność.Oczywiście należy również opisać jak będzie przebiegała operacja obliczania sumy.
'''

# ALGORYTM:     //zakładam że w drzewie są węzły o kluczach x i y!!!
'''
Z każdym węźle trzymamy sumę prawego oraz lewego poddrzewa.
Znajdujemy wspólnego roota dla x i y, a następnie "wspinamy się" do góry z x oraz z y.
Dla węzła x bierzemy sumę prawego poddrzewa (bo elementy są większe niż x), następnie idąc
w górę zwracam uwagę, czy jestem prawym czy lewym synem. Jeżeli prawym - nie dodaję nic,
bo w lewym poddrzewie rodzica są elementy mniejsze. Natomiast jeżeli jestem lewym 
synem, to biorę wartość rodzica oraz sumę jego prawego poddrzewa - są tam elementy większe.
Trzeba wziąć pod uwagę przypadek, gdy x bądź y jest rootem i rozważyć go osobno.
Analogicznie (lecz odwrotnie) idąc od y.
'''


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


# zwracamy ścieżkę od roota do szukanego node'a, dzięki czemu możemy znaleźć wspólnego roota 2 node'ów
def find(root,key,arr):
    while root is not None :
        if root.key==key :
            arr.append(root)
            return root,arr
        elif key > root.key :
            arr.append(root)
            root=root.right
        else:
            arr.append(root)
            root=root.left 
    return None


def sum_between(root,X,Y):
    arr1=[]
    arr2=[]
    x,arr1=find(root,X,arr1)
    y,arr2=find(root,Y,arr2)

    # tam, gdzie wartości w tablicach zaczynają się różnić, tam ścieżki od roota rozdzielają się,
    # czyli ostatnia wspólna wartość to wspólny root
    i=0
    while(arr1[i].key!=arr2[i].key): 
        i+=1
        print(i)
    while( i < min(len(arr1),len(arr2)) and arr1[i].key==arr2[i].key):
        i+=1
    
    common_root=arr1[i-1]

    x_sum=y_sum=0

    if x is not common_root:
        x_sum=x.right_sum

    # aż dojdziemy do roota, bądź okaże się, że rodzic jest za naszym zakresem (x,y) - w przypadku,
    # gdy x lub y jest rootem
    while(x.parent is not common_root and x.parent.key > X):
        # jestem lewym synem - dodaję prawą sumę rodzica
        if x.parent.left is not None and x.parent.left.key==x.key :
            x_sum+=x.parent.right_sum + x.parent.key
            
        x=x.parent
        # w przeciwnym razie idziemy dalej

    if y is not common_root: 
        y_sum=y.left_sum

    while(y.parent is not common_root and y.parent.key < Y):
        # jestem prawym synem - dodaję lewą sumę rodzica
        if y.parent.right is not None and y.parent.right.key==y.key :
            y_sum+=y.parent.left_sum + y.parent.key
            
        y=y.parent
            
    Sum=x_sum+y_sum
    if common_root is not x and common_root is not y:
        Sum+=common_root.key
        
    return Sum
