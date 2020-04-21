# algorytm znajdowania silnie spójnych składowych w grafie skierowanym polega na dwukrotnym użyciu algorytmu DFS;
# uruchamiamy go po raz pierwszy, odwracamy krawędzie w grafie i ponownie uruchamiamy DFS, zważając na to, by w pierwszej 
# kolejności wywoływać go z krawędzi o późniejszym czasie odwiedzenia przez pierwszego DFSa

# reprezentacja grafu przez listy adjacencji
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
    finish=[None]*g.size
    
    def DFSvisit(u):      
        global time
        
        visited[u]=True

        for i in range(1,len(g.arr[u])) :   

            ngh=g.arr[u][i]

            if not visited[ngh] :

                visited[ngh]=True
                DFSvisit(ngh)
         
        # zwiękaszam czas o jedną jednostkę - to czas powrotu
        time+=1
        finish[u]=(time,u)
 
    for v in range(g.size):
        
        if not visited[g.arr[v][0]] : 
            DFSvisit(g.arr[v][0])

    return finish


# odwracamy krawędzi w grafie
def reverse(graph) :
    reversed=Graph(len(graph.arr))

    # krawedz j->i zamieniamy na i->j
    for j in range(len(graph.arr)):
        for i in range(1,len(graph.arr[j])) :
            reversed.add_edge(graph.arr[j][i],j)

    return reversed



def components(graph):

    # dodstajemy tablice czasow przetworzenia pierwszego DFSa - posortowane malejąco  ( krotki postaci: (czas,wierchołek) )
    times=sorted(DFS(graph))[::-1]
    print(time)

    # odwracamy krawedzi w grafie
    rev=reverse(graph)

    def visit(v):    
        comp[counter].append(v)
        vis[v]=True

        for i in range(1,len(rev.arr[v])) :   
            ngh=rev.arr[v][i]

            if not vis[ngh] :                 
                vis[ngh]=True
                visit(ngh)

    vis=[False]*len(graph.arr)
    
    counter=0
    comp=[]   # tablica na poszczególne spójne składowe
    for t in times :   
        v=t[1]

        if not vis[v] :
            comp.append([])
            visit(v)
            counter+=1

    return counter,comp
            

# przykładowe wywołanie

graph=Graph(11)
graph.add_edge(0,2)
graph.add_edge(0,4)
graph.add_edge(1,9)
graph.add_edge(1,0)
graph.add_edge(2,1)
graph.add_edge(3,4)
graph.add_edge(3,6)
graph.add_edge(4,5)
graph.add_edge(5,3)
graph.add_edge(6,5)
graph.add_edge(7,3)
graph.add_edge(8,7)
graph.add_edge(10,8)
graph.add_edge(7,9)
graph.add_edge(9,10)

print()
number,comp=components(graph)
print("number of components: ",number)
print("components: ",comp)
print()
