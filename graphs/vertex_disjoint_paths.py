'''
Dany  jest  graf  skierowany G=  (V, E)  oraz  wierzchołki s i t.  Proszę zaproponować algorytm znajdujący maksymalną 
liczbę rozłącznych (wierzchołkowo) ścieżek między s i t .
'''

# ALGORYTM:

'''
Każdy wierzchołek v rozdzielamy na 2 wierzchołki - v1, do którego wchodzą krawędzi wchodzące do v
oraz v2, z którego wychodzą krawędzi wychodzące z v, dodatkowo między v1 i v2 mamy krawędź (wierzchołek s i t 
rozdzielimy również, chociaż nie jest to konieczne, ale łatwiej zaimplementować algorytm) Każda z krawędzi grafu 
ma przepustowość równą 1, tylko dla s i t przepustowość ustalamy jako inf. Dzięki temu znajdując maksymalny 
przepływ w tak zmodyfikowanym grafie dostaniemy liczbę ścieżek rozłącznych wierzchołkowo. A to dlatego, że gdy przez 
daną krawędź łaczącą rozdzielony wierzchołek v puścimy przepływ (czyli jedną ze ścieżek), to mamy pewność, że 
już żadna tamtędy nie będzie przebiegać (ponieważ) przepustowość wynosiła 1. To daje nam gwarancję, że wszystkie 
ścieżki będą rozłączne wierzchołkowo.
'''

class graph:

    def __init__(self,size):
        self.m=[[0]*size for i in range(size)] 
        self.size=size
    
    def add_edge(self,v,u):
        self.m[v][u]=1
    
    def printG(self):
        for i in self.m:
            print(i)


from factories_and_stores import Ford_Fulkerson


def paths(g,s,t):
    # tworzymy nową macierz powiększoną rozmiar grafu (bo każdy wierzchołek rozdzielamy na 2)
    matrix=[[0]*(2*g.size) for _ in range(2*g.size)]

    # każdy wierchołek v rozdzielamy na dwa - w nowej macierzy odpowiednio 2*v oraz 2*v+1
    for i in range(g.size):
        for j in range(g.size):
            if g.m[i][j] != 0:
                matrix[2*i+1][2*j]=1
    
    for v in range(g.size):
        if v==s or v==t:
        # przepustowość dla źródła i ujścia ustalamy jako inf
            matrix[2*v][2*v+1]=float("inf")
        else: 
            matrix[2*v][2*v+1]=1


    for i in matrix:
        print(i)

    return Ford_Fulkerson(matrix,2*s,2*t+1)
