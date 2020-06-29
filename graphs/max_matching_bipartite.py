# algorytm znajdujący maksymalne skojarzenie w grafie dwudzielnym

'''
Mając 2 zbiory wyznaczone przez graf dwudzielny (A i B) możemy wyznaczyć maksymalne skojarzenie poprzez dodanie
super-źródła i super-ujścia i założenie, że każda krawędź ze zbioru A jest skierowana do zbioru B oraz jej
przepustowość wynosi 1. Maksymalnym skojarzeniem jest maksymalnym przepływ od super-źródła do super-ujścia.
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


# algorytm do znajowania max przepływu w grafie skierowanym 
from factories_and_stores import Ford_Fulkerson


def max_matching(g):

    # tworzymy nową macierz, gdzie super-źródło(S) ma indeks len(matrix)-2, a super-ujście(T) - len(matrix-1)
    
    matrix=[[0]*(len(g.m)+2) for _ in range(len(g.m)+2)]

    S=len(matrix)-2
    T=len(matrix)-1

    for i in range(len(g.m)):
        for j in range(len(g.m)):
            matrix[i][j]=g.m[i][j]

            # dodajemy krawędzi od super-źródła i do super-ujścia
            if g.m[i][j] == 1:
                matrix[S][i]=1
                matrix[j][T]=1

    return Ford_Fulkerson(matrix,S,T)
