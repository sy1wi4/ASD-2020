# DEPTH FIRST SEARCH

# algorytm z użyciem listy sasiedztwa (adjacencji)

class graph:
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
            
time=0

def DFS(g):
    visited=[False]*g.size
    entry=[None]*g.size
    finish=[None]*g.size
    parent=[None]*g.size

    def DFSvisit(u):      
        global time
        time+=1    # zwiekszam o 1 jednostke czasu, gdy wywoluje dla kolejnych
        visited[u]=True
        entry[u]=time
        for i in range(1,len(g.arr[u])) :    # odwiedzamy wszystkich sąsiadów wierzchołka u
            
            ngh=g.arr[u][i]

            if not visited[ngh] :

                visited[ngh]=True
                parent[ngh]=u
                DFSvisit(ngh)
                
        # kiedy juz przejde wszystkich sasiadow, i skonczy sie petla, to 
        # zwiekaszam czas o jedna jednostke - to czas powrotu
        
        time+=1
        finish[u]=time

    # wywolujemy z kazdego wiercholka funkcje visit, bo za jednym razem
    # mozemy nie przejsc calego grafu
    
    for v in range(g.size):
        
        if not visited[g.arr[v][0]] : 
            DFSvisit(g.arr[v][0])

    return entry,finish,parent


g=graph(5)
g.add_edge(1,4)
g.add_edge(1,2)
g.add_edge(0,2)
g.add_edge(4,0)
g.add_edge(4,3)
g.printG()
print(DFS(g))
