'''
Dany  jest  graf  nieskierowany G oraz  dwa  jego  wierzchołki s i t.  Proszę zaproponować algorytm, 
który sprawdza czy istnieje taka krawędź, po usunięciu której długość najkrótszej ścieżki z s do t 
(lub taka ścieżka przestaje istnieć).
'''

# ALGORYTM: 
'''
Obliczamy ilość najkrótszych ścieżek między s i t przy użyciu BFSa. Budujemy graf najkrótszych ścieżek
i jeżeli jest w nim jakiś most, to znaczy, że istnieje psująca ścieżka.
'''

from collections import deque

class graph:

    def __init__(self,size):
        self.m=[[0]*size for i in range(size)]  # macierz sasiedztwa
        self.size=size
    def add_edge(self,v,u):
        self.m[v][u]=1
        self.m[u][v]=1
    
    def printG(self):
        for row in self.m:
            print(row)

def BFS(g,s,t):  # przekazujemy startowy wiercholek
    
    q=deque()
    number=len(g.m)
    
    # tworzymy pomocnicza tablice czy odwiedzony
    visited=[False]*number

    # tablica na rodzicow
    parents=[[None]for _ in range(number)]
    # tablica na najkrotsza sciezke od s do v
    dist=[0]*number

    # tablica na liczbę ścieżek z s do v
    paths=[0]*number
    paths[s]=1

    q.appendleft(s)  
    visited[s]=True

    while(len(q)!=0):
        u=q.pop()

        #przegladamy wszystkie wierzcholki polaczone z u
        for i in range(number):
            if len(q)==0 : q=deque()

            # jezeli istnieje nieodwiedzona krawedz
            if g.m[u][i]==1 : 

                # jeśli nieodwiedzony, to tyle samo ścieżek ile ten, z którego przyszliśmy
                if visited[i]==False :
                    parents[i]=[u]
                    visited[i]=True
                    dist[i]=dist[u]+1
                    paths[i]=paths[u]
                    q.appendleft(i)
                
                # jeśli odwiedzony, to sprawdzamy czy ścieżka z aktualnego wierzchołka jest tej samej
                # długości co dotychczas najkrótsza, jeśli tak to zwiększamy liczbę ścieżek o ścieżki do aktualnego
                else:
                    if dist[i] == dist[u]+1:
                        paths[i] += paths[u]
                        parents[i].append(u)

    # zwracamy ilość najkrótszych ścieżek do t i ich długość
    return parents,dist[t],paths[t]



time=0

def find_bridge(g):
    visited=[False]*g.size
    parents=[None]*g.size
    entry=[None]*g.size
    low=[None]*g.size
    
    def DFSvisit(u):      
        global time
        time+=1
        entry[u]=time
        low[u]=time
        visited[u]=True

        for i in range(1,len(g.arr[u])) :   

            ngh=g.arr[u][i]

            if not visited[ngh] :
                parents[ngh]=u
                visited[ngh]=True
                DFSvisit(ngh)

                # przy powrocie rekurencji  (gdy już odwiedzimy wszystkie
                #  dzieci) sprawdzamy czy niżej była jakaś krawędź wsteczna 
                low[u]=min(low[u],low[ngh])
            
            elif visited[ngh] and parents[u] != ngh :
                # krawędź wsteczna do ngh, który już został odwiedzony
                low[u]=min(low[u],entry[ngh])
        
         
    for v in range(g.size):
        
        if not visited[g.arr[v][0]] : 
            DFSvisit(g.arr[v][0])

    bridges=[]

    for i in range(g.size) :
        if entry[i] == low[i] and parents[i] is not None:
            # mamy most
            bridges.append((parents[i],i))
    #print("b",bridges)
    return len(bridges) >= 1


class Graph:
    def __init__(self,size):
        self.size=size
        self.arr=[[i] for i in range(size)]

    def add_edge(self,v,u): 
        self.arr[v].append(u)

    def printG(self):
        print("\n")
        for i in self.arr:
            for j in i:
                print(j,end=" ")
            print("\n")


# zamiana sposobu reprezentacji grafu z macierzy na listy
def matrix_to_lists(g):
    new=Graph(g.size)
    for i in range(g.size):
        for j in range(g.size):
            if i<j and g.m[i][j] != 0:
                new.add_edge(i,j)
                new.add_edge(j,i)
    
    return new


def path_spoilage(g,s,t):
    parents,dist,paths=BFS(g,s,t)   # tablica parentów, długość ścieżki, liczba ścieżek

    new_graph=graph(g.size)

    idx=0   # którego z parentów biorę

    while idx < paths:

        current=t       # aktualny wierzchołek

        for _ in range(dist):

            # jeśli mamy na tyle parentów, to bierzemy 
            # ten o indeksie idx, jeśli nie, to ostatniego

            if idx < len(parents[current]):
                prev=parents[current][idx]
            else:
                prev=parents[current][-1]
            
            new_graph.add_edge(current,prev)
            current=prev

        idx += 1
    
    new_g=matrix_to_lists(new_graph)
    new_g.printG()
    # jeżeli w grafie najkrótszych ścieżek jest jakikolwiek most, to zwracamy True
    return find_bridge(new_g)
