'''
Proszę wskazać algorytm, który znajduje maksymalny przepływ między źródłem i ujściem w grafie nieskierowanym.

'''

# ALGORYTM:
'''
Oryginalny algorytm działa tylko dla grafów, w których nie istnieją krawędzi (skierowane) w dwie strony. W takim razie
każdą krawędź nieskierowaną zamieniamy w następujący sposób: w jedną stronę tworzymy krawędź skierowaną, a w drugą dodajemy 
wierzchołek i dodajemy 2 skierowane krawędzi. Przepustowość nowych krawędzi jest taka sama jak oryginalnej nieskierowanej.
Dzięki tej modyfikacji możemy użyć podstawowego algorytmu do szukania maksymalnego przepływu.
'''

class graph:

    def __init__(self,size):
        self.m=[[0]*size for i in range(size)] 
        self.size=size
        self.edges=0       # dla ułatwienia licznik krawędzi grafu
    
    def add_edge(self,v,u,weight):
        self.m[v][u]=weight
        self.m[u][v]=weight
        self.edges+=1
    
    def printG(self):
        for i in g.m:
            print(i)


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

#########################################################################################
############################### główny algorytm #########################################
#########################################################################################


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
