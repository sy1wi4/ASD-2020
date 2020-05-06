'''
Dany jest graf ważony. Wagę ścieżki definujemy jako min(z wag krawędzi na tej ścieżce) 
znaleźć najdłuższą ścieżkę między wierzchołkami s i t.
'''

# ALGORYTM:

'''
Zaczynamy od samych wierzchołkow bez krawędzi. W kolejności dokładamy krawędzi o coraz mniejszych
wagach i sprawdzamy, czy zaistniała ścieżka między s i t. Pierwsza krawędź, dla której znajdziemy taką
ścieżkę jest wagą najdłuższej ścieżki. Algorytm ten jest poprawny, ponieważ każda kolejna ścieżka, 
którą byśmy znaleźli będzie miała mniejszą wagę (zostanie utworzona po dołożeniu lżejszej krawędzi).
Czy istnieje ścieżka z s do t będziemy sprawdzali przy użyciu struktury zbiorów rozłącznych (find/union).
'''

# reprezentacja grafu przez listy adjacencji
class Graph:
    def __init__(self,size):
        self.size=size
        self.arr=[[i] for i in range(size)]
        self.edges=[]

    def add_edge(self,v,u,w):
        self.arr[v].append((u,w))
        self.edges.append((w,v,u))  # tablica krawędzi z v do u w postaci krotek (waga,v,u)
        
        
# struktura zbiorów rozłacznych
class Node:
    def __init__(self,id):
        self.id=id
        self.parent=self    
        self.rank=0        

# zwraca reprezentanta zbioru zawierajacego x
def find_set(x) :
    if x != x.parent :
        # rekurencyjnie "pniemy" sie w gore drzewa, dokonując jednocześnie kompresji ścieżki
        x.parent=find_set(x.parent)
    return x.parent 

# łączy 2 zbiory w 1 (ten o mniejszej randze dołączamy do tego o większej)
def union(x,y):
    x=find_set(x)
    y=find_set(y)

    if x.rank > y.rank :
        y.parent=x
        
    elif y.rank > x.rank:
        x.parent=y

    else :
        x.parent=y
        y.rank+=1    # po złączeniu drzew o tych samych rozmiarach zwiększamy rangę o 1

#--------------------------------------------------------------------------------------------------------

def find_max_path(g,s,t):
    # na początku każdy wierzchołek jest osobnym zbiorem
    sets=[]
    for i in range(g.size):
        sets.append(Node(i))

    # sortujemy krawędzi niemalejąco
    g.edges=sorted(g.edges)[::-1]    

    # kolejno bierzemy krawędzi i wierzchołki do niej należace łączymy w jeden zbiór przy pomocy union,
    # następnie sprawdzamy, czy s i t należą po tej operacji do jednego zbioru - jeśli tak, to waga tej 
    # krawędzi jest wagą szukanej najdłuższej ścieżki

    for e in g.edges:
        weight=e[0]
        v=e[1]
        u=e[2]

        # łączymy zbiory u i v
        union(sets[v],sets[u])

        if find_set(sets[s]) == find_set(sets[t]) :
            return weight
   
