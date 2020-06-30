'''
Dany jest grafG=(V, E), gdzie każda krawędź ma wagę ze zbioru{1,...,|E|} (wagi krawędzi są parami różne). 
Proszę zaproponować algorytm, który dla danych wierzchołków x i y oblicza ścieżkę o najmniejszej sumie wag, 
która prowadzi z x do y po krawędziach o malejących wagach (jeśli ścieżki nie ma to zwracamy inf). 
'''

# ALGORYTM:

'''
Sortujemy malejąco krawędzi, następnie wykonujemy relaksację krawędzi w tej kolejności. 
Algorytm jest poprawny dlatego, że na początek w tablicy odległości każdy wierchołek oprócz
startowego (x) ma przypisaną wartość inf, dzięki temu relaksacja rozpocznie się tak naprawdę
od najdłuższej krawędzi wychodzącej z x. Następnie relaksujemy coraz krótsze krawędzi, a więc
mamy pewność, że odległość jaka po przejściu algorytmu jest dla wierzchołka końcowego y jest 
najkrótszą ścieżką przechodzącą po krawędziach o malejących wagach.
'''

class Graph:
    def __init__(self,size):
        self.size=size
        self.arr=[[] for _ in range(size)]
        self.edges=[]

    def add_edge(self,v,u,weight): # krawedz z v do u
        self.arr[v].append([u,weight])      # tworzymy krotki (u,waga krawedzi z v do u)
        self.edges.append((v,u,weight))

    def printG(self):
        print("\n")
        v=0
        for i in self.arr:
            print(v,i)
            v+=1
            print("\n")


# relaksacja krawędzi z u do v
def relax(u,v,weight,parent,distance) :
    
    if distance[v]>distance[u]+weight:
        distance[v]=distance[u]+weight
        parent[v]=u


def path(g,s,t):
    # sortujemy krawędzi grafu po wagach krawędzi malejąco
    sorted_edges=sorted(g.edges, key = lambda x:x[2] ,reverse=True )

    distance=[float("inf")]*g.size
    distance[s]=0
    parents=[None]*g.size

    for edge in sorted_edges :
        relax(edge[0],edge[1],edge[2],parents,distance)

    # wypisujemy ścieżkę
    if distance[t] != float("inf"):
        curr=t
        while(curr is not None):
            print(curr)
            curr=parents[curr]

    return distance[t]
