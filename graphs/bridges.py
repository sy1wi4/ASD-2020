'''
    Wywołujemy DFS, zapisując czas odwiedzenia każdego wierzchołka,
    obliczamy low, gdzie low = min( d(u) , d(v) , min(low(w)) ), gdzie
    u to wierzchołek do którego mamy krawędż wsteczną w drzewie DFS, 
    a w to dziecko v w drzewie DFS.
    Mosty to krawędzie, gdzie d(v) = low(v)
'''

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


time=0

def DFS(g):
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

    return bridges


#-----------------
g=Graph(8)
g.add_edge(0,1)
g.add_edge(1,0)
g.add_edge(0,6)
g.add_edge(6,0)
g.add_edge(3,2)
g.add_edge(2,3)
g.add_edge(2,6)
g.add_edge(6,2)
g.add_edge(6,7)
g.add_edge(7,6)
g.add_edge(4,3)
g.add_edge(3,4)
g.add_edge(2,1)
g.add_edge(1,2)
g.add_edge(3,5)
g.add_edge(5,3)
g.add_edge(4,5)
g.add_edge(5,4)


bridges=DFS(g)
print("bridges: ",bridges)
