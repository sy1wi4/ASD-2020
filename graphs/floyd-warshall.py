# ALGORYTM FLOYDA-WARSHALLA
# najkrótsze ścieżki między każdą parą wierchołków (w szczególności dla grafów gęstych)

# Działa on w sposób dynamiczny i opiera się na spostrzeżeniu, że jeśli koszt dojścia z wierzchołka v  do u
# jest większy od sumy kosztów dojść z wierzchołka v  do k  i z k  do u, to za lepszy koszt należy przyjąć tę
# nową, mniejszą wartość. (Dopuszczamy wagi ujemne, ale nie może być ujemnego cyklu)

# dla grafów rzadkich możemy V razy wywołać algorytm Dijkstry lub Bellmana-Forda


# reprezentacj macierzowa grafu
class graph:

    def __init__(self,size):
        self.size=size
        self.m=[[0]*size for i in range(size)]  # macierz sasiedztwa
    
    def add_edge(self,v,u,weight):
        self.m[v][u]=weight



def floyd_warshall(g):

    # tworzymy macierz odległości, gdzie dist[u][v] to długość najkrótszej ścieżki z u do v
    dist=g.m

    for i in range(g.size):
        for j in range(g.size):
            if dist[i][j]==0 and i!=j :
                dist[i][j]=float("inf")

    # sprawdzamy, czy scieżka z u do v jest krótsza z wykorzystaniem wierchołka s czy nie
    for s in range(g.size) :
        for u in range(g.size) :
            for v in range(g.size) :
                dist[u][v]=min(dist[u][v],dist[u][s]+dist[s][v])
                
    return dist
