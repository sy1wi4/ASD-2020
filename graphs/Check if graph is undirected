''' Proszę podać algorytm, który mając na wejściu graf G reprezentowany
przez listy sąsiedztwa sprawdza, czy dla każdej krawędzie u → v istnieje także krawędź przeciwna '''

# reprezentacja przez listy sasiedztwa 

class Graph:
    def __init__(self,size):
        self.size=size
        self.arr=[[i] for i in range(size)]

    def add_edge(self,v,u): # krawedz z v do u
        self.arr[v].append(u)

    def printG(self):
        print("\n")
        for i in self.arr:
            for j in i:
                print(j,end=" ")
            print("\n")



def isUndirected(g):
    res=[0]*len(g.arr)
    for v in g.arr :                # przegladamy listy adjacencji kazdego wierzcholka
        res[v[0]]-=(len(v)-1)       # o tyle ile krawedzi wychodzi zwiekszamy wartosc w tablicy 
        for vertex in v[1:] :
            res[vertex]+=1          # kazdy wierzcholek do ktorego idzie krawedz - zmniejszamy o 1
    
    for el in res:
        if el != 0 : return False
    
    return True

g=Graph(4)
g.add_edge(0,3)
g.add_edge(3,0)
g.add_edge(1,2)
g.add_edge(2,1)
g.add_edge(2,3)
g.add_edge(3,2)
g.printG()
print(isUndirected(g))
