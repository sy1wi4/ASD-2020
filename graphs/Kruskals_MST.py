# MINIMUM SPANNING TREE   O(ElogV)

# algorytm polega na posortowaniu krawędzi w porządku niemalejącym, następnie kolejno każdą krawędź 
# próbujemy dołożyć do minimalnego drzewa rozpinającego, warunkiem jest to, że nie może ona tworzyć
# cyklu z już istniejącym MST - sorawdzamy to używając struktury zbiorów rozłacznych FIND-UNION

# Find/Union
class Node:
    def __init__(self,id):
        self.id=id
        self.parent=self    # na poczatku mamy zbiory jednoelementowe, wiec jako rodzic el. wskauja samych siebie  
        self.rank=0         # wysokkosc drzewa

# zwraca rerezentanta zbioru zawierajacego x
def find_set(x) :
    if x != x.parent :
        # rekurencyjnie "pniemy" sie w gore drzewa
        x.parent=find_set(x.parent)
    return x.parent # na samej gorze korzystamy z tego ze rodzic x to x

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
        y.rank=1    # po złączeniu drzew o tych samych rozmiarach zwiększamy rozmiar o 1


class Graph:
    def __init__(self,size):
        self.size=size
        self.arr=[[i] for i in range(size)]
        self.edges=[]
        

    def add_edge(self,v,u,weight): # krawedz z v do u
        self.arr[v].append((u,weight))
        self.edges.append((weight,v,u))
        

    def printG(self):
        print("\n")
        for i in self.arr:
            for j in i:
                print(j,end=" ")
            print("\n")




def MST_Kruskal(g):
    # tworzymy posortowaną tablicę krawędzi u->v w postaci krotek (waga,u,v)
    g.edges=sorted(g.edges)
    print(g.edges)
    
    MST=[]   # tablica przechowująca krawędzi MST
    sets=[]  # tablica przechowująca zbiór do którego należy dany wierzchołek

    # z każdego wierchołka robimy osobny zbiór
    for i in range(g.size):
        sets.append(Node(i))
    
    for v in sets:
        print(v.id,v.parent.id)

    # kolejno po wybieramy krawędzi o najmniejszych wagach i jeśli nie tworzą one cyklu z poprzednio
    # wybranymi, to dodajemy je do MST

    for edge in g.edges:

        # wierzchołki połączone aktualnie rozważaną krawędzią
        u=edge[1]
        v=edge[2]
        
        if find_set(sets[u]) != find_set(sets[v]) :
            # nowa krawedź nie stworzy cyklu - dodajemy do MST
            MST.append(edge)
            union(sets[u],sets[v])

    return MST
