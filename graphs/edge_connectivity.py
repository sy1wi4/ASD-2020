'''
Dany jest graf nieskierowany G = (V, E). Mówimy, że spójność krawędziowa G wynosi k jeśli usunięcie pewnych
k krawędzi powoduje, że G jest niespójny, ale usunięcie dowolnych k−1 krawędzi nie rozspójnia go. 
Proszę podać algorytm, który oblicza spójność krawędziową danego grafu.
'''

# ALGORYTM:
'''
By znaleźć spójność krawędziową wystarczy założyć, że każda z krawędzi ma przepustowość 1, a następnie
z jakiegoś wierzchołka u znaleźć maksymalny przepływ do każdego innego (V-1 razy max flow). Spójność
krawędziowa to najmniejszy z maksymalnych przepływów - usunięcie tylu krawędzi gwarantuje rozspójnienie grafu.
Algorytm jest poprawny, ponieważ jeżeli znamy maksymalny przepływ do każdego wierzchołka, to wiemy ile 
minimalnie musimy usunąć krawędzi, aby nie było między nimi żadnej ścieżki. A biorąc najmniejszy z nich 
uzyskujemy minimalną liczbę krawędzi potrzebną do rozspójnienia grafu.
Wykorzystujemy algorytm do znajdowania maksymalnego przepływu w grafie NIEskierowanym (z dodatkowymi wierchołkami).
'''

###################################################################################
############ algorytm do znajdowania max flow w grafie nieskierowanym #############
###################################################################################

from collections import deque

def BFS(g,s,t,parents):  
    
    q=deque()
    number=len(g)

    visited=[False]*number
    q.appendleft(s)  
    visited[s]=True

    while(len(q)!=0):
        u=q.pop()
        
        for i in range(number):
            if len(q) == 0 : q=deque()
            if(g[u][i]!=0 and visited[i]==False) :  
                parents[i]=u
                visited[i]=True
                q.appendleft(i)
    
                
    return visited[t]


# maksymalny przepływ z wierzchołka s do t
def Ford_Fulkerson(g,s,t):

    parents=[None]*len(g)
    flow=0

    while BFS(g,s,t,parents):
      
        current=t
        cur_flow=float("inf")

        while(current!=s):
            if g[parents[current]][current] < cur_flow :
                cur_flow=g[parents[current]][current] 
            current=parents[current]
        
        flow += cur_flow
        v=t

        while(v!=s):
           
            g[parents[v]][v]-=cur_flow
            g[v][parents[v]]+=cur_flow
            v=parents[v]
    return flow

def flow(g,s,t):

    # najpierw musimy powiększyć graf o tyle wierzchołków, ile graf ma krawędzi

    matrix=[[0]*(g.size+g.edges) for _ in range(g.size+g.edges)]
    
    current=g.size    # nr wierzchołka, który aktualnie dodajemy
    for i in range(g.size):
        for j in range(g.size):
            if i < j and g.m[i][j] != 0 :
                # rozważamy krawędź i - j
                matrix[i][j]=g.m[i][j]   # krawędź i -> j  
                matrix[j][current]=matrix[current][i]=g.m[i][j]   # krawędź j -> i rozdzielona dodanym wierzchołkiem
                current+=1
    
    # na nowoutworzonej macierzy uruchamiamy algorytm wyznaczający maksymalny przepływ w grafie skierowanym

    return Ford_Fulkerson(matrix,s,t)


###################################################################################
###################################################################################
###################################################################################

class graph:

    def __init__(self,size):
        self.m=[[0]*size for i in range(size)] 
        self.size=size
        self.edges=0
    
    def add_edge(self,v,u):
        self.m[v][u]=1
        self.m[u][v]=1
        self.edges+=1
    
    def printG(self):
        for i in g.m:
            print(i)

def edge_connectivity(g):
    min_flow=float("inf")
    
    # szukamy max flow dla par wierchołków 0 - v
    for v in range(1,len(g.m)):
        max_flow=flow(g,0,v)
        if max_flow < min_flow :
            min_flow = max_flow
    
    return min_flow
