''' 
Przewodnik chce przewieźć grupę turystów z miasta A do miasta B. Po drodze jest
jednak wiele innych miast i między różnymi miastami jeżdzą autobusy o różnej pojemności. 
Mamy daną listę trójek postaci (x, y, c), gdzie x i y to miasta między którymi bezpośrednio
jeździ autobus o pojemności c pasażerów. Proszę zaproponować algorytm, który znajduje trasę 
z A do B, po której może przejechać możliwie jak największa grupa turystów bez rozdzielania się.
'''

# ALGORYTM:

# 1. używamy algorytmu podobnego do Dijkstry, z tym, że używamy kolejki priorytetowej typu max 
#    a "relaksacja" krawędzi z u do v polega na tym, że bierzemy minimum z [wagi krawędzi] oraz
#    [większej z wag przypisanych do wierchołków u i v], dzięki czemu weźmiemy największą z możliwych
#    dostępnych pojemności - czyli szukaną liczebność grupy

# 2. szukamy "maksymalnego" drzewa rozpinającego - jego krawędź o najmniejszej wadze to szukana grupa

# 3. BISEKCJA+DFS
#    sortujemy po długościach krawędzie rosnąco, biorę jako przypuszczalnie szukaną wartość środkową i
#    i nie biorąc pod uwagę krawędzi o mniejszej wadze, puszcam DFS i sprawdzam czy zdoła on 
#    odwiedzić miasto B. Jeśli tak, to sprawdzam wartość będącą w połowie stawki powyżej wziętej
#    poprzednio krawędzi, analogicznie jeśli nie - poniżej.



# sposób nr 2 - korzystamy z algorytmu analogicznego do algorytmu Prima, tylko bierzemy krawędzi
# o maksymalnych wagach

# ponieważ korzystamy z kolejki priorytetowej o priorytecie min, to aby wyciągać krawędzi o 
# maksymalnych wagach dokonujemy modyfikacji - wstawiamy do kolejki wagi przeciwne (minus)

class Graph:
    def __init__(self,size):
        self.size=size
        self.arr=[[i] for i in range(size)]

    def add_edge(self,v,u,weight): # krawędź z v-u
        self.arr[v].append((weight,u))
        self.arr[u].append((weight,v))

    def printG(self):
        print("\n")
        for i in self.arr:
            for j in i:
                print(j,end=" ")
            print("\n")


from queue import PriorityQueue 

def MST_Prim(g,s):
    q=PriorityQueue()
    visited=[False]*g.size


    # do kolejki wszystkie wierzchołki z wagą inf, startowy z wagą 0
    for v in range(g.size):
        if v != s: q.put((float("inf"),v))
    q.put((0,s))

    max_weight=[float("-inf")]*g.size
    max_weight[s]=0
    parents=[None]*g.size

    while not q.empty() :
        u=q.get()[1]
        visited[u]=True     # oznaczam jako przetworzony

        for v in g.arr[u][1:] :
           if not visited[v[1]]:
                # aktualizuję wagi
                if v[0] != float("inf") and max_weight[v[1]] < v[0] :
                    max_weight[v[1]] = v[0]
                    parents[v[1]]=u 
                    q.put((-1*v[0],v[1]))


    return parents


def tour_guide(arr,A,B):
    g=Graph(5)
    for edge in arr:
        g.add_edge(edge[0],edge[1],edge[2])

    # wyznaczamy maksymalne drzewo rozpinające
    parents=MST_Prim(g,0)
    
    # najmniejsza z wag krawędzi z MST na ścieżce od B do A (idąc po parentach) to maksymalna wielkość grupy
    # nas interesuje nas tylko sama ścieżka - łatwo ją wyznaczyć mając tablicę parentów

    current=B
    path=[B]
    while current != A:
        path.append(parents[current])
        current=parents[current]

    return path
