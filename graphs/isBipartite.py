''' Sprawdzanie czy graf nieskierowany jest dwudzielny (czyli czy da się podzielić jego 
wierzchołki na dwa zbiory, takie że krawędzie łączą jedynie wierzchołki z różnych zbiorów) '''

# robimy BFS (lub DFS) przydzielajac wiercholkom "kolory"


from collections import deque

def isBipartite(G,s):   # s - wierzcholek startowy
    q=deque()
    color=[None]*len(G.arr)
    visited=[False]*len(G.arr)
    q.appendleft(s)
    visited[s]=True
    color[s]=0
    while(len(q)!=0):
        if len(q)==0 : q=deque()            
        a=q.pop()
        
        for el in G.arr[a][1:] :    # przegladamy wszystkich sasiadow (w danym wierszu indeksy od 1 do konca)
            if color[el]==color[a] : return False,color
            elif not visited[el] :
                visited[el]=True
                color[el]=1-color[a]      # dzieki temu naprzemian przypisujemy kolory 0 i 1
                q.appendleft(el)
        
    return True,color



# reprezentacja poprzez listy adjacencji

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

G=graph(4)
G.add_edge(1,0)
G.add_edge(1,2)
G.add_edge(0,2)
G.add_edge(3,2)
G.add_edge(1,3)
G.add_edge(0,1)
G.add_edge(2,1)
G.add_edge(2,0)
G.add_edge(2,3)
G.add_edge(3,1)
G.printG()
print(isBipartite(G,0))
