# MINIMUM SPANNING TREE   O(ElogV)
# graf nieskierowany

# bardzo podobny do algprytmu Dijkstry

# dla każdego wierzchołka będziemy pamiętać min wagę dojścia z sąsiedniego
# wierzchołka oraz rodzica

#  -> wszystkie wierzchołki umieszczamy w kolejce priorytetowej z wagą inf
#     a wierzchołek  startowy z wagą 0
#  -> póki kolejka nie jest pusta wyciągamy wierzchołek i dla każdego sąsiada
#  -> uaktualniamy wagę - dodając ten wierchołke do kolejki ponownie z nową wagą
#     (jeśli waga danej krawędzi jest mniejsza niż obecna waga)oraz parenta


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

    min_weight=[float("inf")]*g.size
    min_weight[s]=0
    parents=[None]*g.size

    print(q.queue)

    while not q.empty() :
        u=q.get()[1]
        visited[u]=True     # oznaczam jako przetworzony

        for v in g.arr[u][1:] :
           if not visited[v[1]]:
               # aktualizuję wagi
                if min_weight[v[1]]>v[0] :
                    min_weight[v[1]]=v[0]
                    parents[v[1]]=u
                    q.put((v[0],v[1]))

    # szukane drzewo rozpinające tworzą krawędzi łaczące wierzchołki ze swoimi rodzicami
    MST=[]
    for i in range(g.size):
        if parents[i] is not None :
            MST.append((parents[i],i,min_weight[i]))

    return MST
