'''
Dany jest graf G. Podaj jak najszybszy algorytm, który tworzy podgraf G’ zawierający
taki podzbiór krawędzi i wierzchołków z G, że każdy wierzchołek w G’ ma stopień co najmniej k.
Uwaga!: przemyśl parę razy pierwsze rozwiązanie, które przyjdzie Ci do głowy.
'''

# rozwiązanie nieoptymalne:

# usuwamy wierzchołki o stopniu mniejszym od k i dekrementujemy też stopnie sąsiadów,
# powtarzamy aż dotąd, gdy w którymś przejściu nic nie usuniemy


# rozwiązanie optymalne:

# kolejka priorytetowa ze stopniem jako k
# wyciagnij wierzcholek z kopca i jesli ma stopien < k, to 
# dekrementujemy sąsiadów (w kopcu)
# E razy heapify przy dekrementacji wag sąsiadów 

# O(ElogV) 



class graph:
    def __init__(self,size):
        self.size=size
        self.arr=[[i] for i in range(size)]

    def add_edge(self,v,u): # krawedz z v do u
        self.arr[v].append(u)
        self.arr[u].append(v)

    def printG(self):
        print("\n")
        for i in self.arr:
            for j in i:
                print(j,end=" ")
            print("\n")


from queue import PriorityQueue

def subgraph(g,k):
    q=PriorityQueue()

    # w tablicy przechowujemy aktualne stopnie wierzchołków,
    # by móc je "aktualizować" w kolejce
    degrees=[None]*g.size

    # tablica usuniętych wierzchołków
    removed=[False]*g.size

    # wszystkie wierzchołki umieszczamy w kolejce ze stopniem jako klucz
    for v in range(g.size):
        degree=len(g.arr[v])-1
        q.put((degree,v))
        degrees[v]=degree


    deg,u=q.get()
    while(deg < k):
        # jeśli stopień wierzchołka jest mniejszy od k, to zmniejszamy stopień
        # wszystkich jeszcze nieusuniętych sąsiadów o 1 i wstawiamy zaktualizowane do kolejki
        for v in g.arr[u][1:] :
            if not removed[v]:
                q.put((degrees[v]-1,v))
            
  
    return removed
