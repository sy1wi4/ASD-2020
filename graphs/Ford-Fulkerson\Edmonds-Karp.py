# metoda Forda-Fulkersona polega na zwiększaniu wartości 
# przepływu dopóki istnieje ścieżka z s do t (w sieci rezydualnej -
# należą do niej te krawędzi, których przepustowość rezydualna jest
# >0). Dopóki jesteśmy w stanie znaleźć ścieżkę powiększającą, robimy to.

# to tak naprawdę algorytm Edmondsa-Karpa -> używa BFSa
# do szukania ścieżek, lecz opiera się na metodzie Forda-Fulkersona

# reprezentacja macierzowa grafu

class graph:

    def __init__(self,size):
        self.m=[[0]*size for i in range(size)] 
        self.size=size
    
    def add_edge(self,v,u,weight):
        self.m[v][u]=weight
    
    def printG(self):
        for i in g.m:
            print(i)


class node:
    def __init__(self):
        self.val=None
        self.next=None

class queue:
    def __init__(self):
        self.head=node()
        self.tail=node()

    def enqueue(self,x):    
        n=node()
        if self.tail.next==None :     
            self.head.next=n
            self.tail.next=n
            n.next=None
            n.val=x
        else:    
            self.tail.next.next=n    
            n.next=None         
            n.val=x             
            self.tail.next=n         
   
    def dequeue(self):     
        n=self.head.next 
        self.head.next=n.next
        return n.val

    def is_empty(self):
        return self.head.next==None

def BFS(g,s,t,parents):  
    
    q=queue()
    number=len(g.m)

    visited=[False]*number
    q.enqueue(s)  
    visited[s]=True

    while(not q.is_empty()):
        u=q.dequeue()
        
        for i in range(number):
            if q.is_empty() : q=queue()
            if(g.m[u][i]!=0 and visited[i]==False) :  
                parents[i]=u
                visited[i]=True
                q.enqueue(i)
                
    return visited[t]

#--------------------------------------------------------------------

# maksymalny przepływ z wierzchołka s do t
def Ford_Fulkerson(g,s,t):

    parents=[None]*g.size
    flow=0

    while BFS(g,s,t,parents):
       
        # szukamy krawędzi o najmniejszej pojemności rezydualnej (czyli
        # największego przepływu jaki może być na danej ścieżce)
        # idziemy od ujścia po parentach w górę
        current=t
        cur_flow=float("inf")

        while(current!=s):
            if g.m[parents[current]][current] < cur_flow :
                cur_flow=g.m[parents[current]][current] 
            current=parents[current]
        
        # po przejściu ścieżki zwiększamy flow o najmniejszą pojemność
        # rezydualną na tej ścieżce (cur_flow)
        flow += cur_flow

        # aktualizujemy pojemności rezydualne istniejących krawędzi oraz
        # krawędzi powrotnych, znowu idziemy od ujścia po parentach w górę
        v=t

        while(v!=s):
            g.m[parents[v]][v]-=cur_flow
            g.m[v][parents[v]]+=cur_flow
            v=parents[v]
    #g.printG()
    return flow
