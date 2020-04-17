# BREADTH FIRST SEARCH
# algorytm z uzyciem macierzy sasiedztwa 

# bedziemy potrzebowali kolejki, aby tam umieszczac wierzcholki

class node:
    def __init__(self):
        self.val=None
        self.next=None

class queue:
    def __init__(self):
        self.head=node()
        self.tail=node()
    
    # put
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
    
    # get
    def dequeue(self):     
        n=self.head.next 
        self.head.next=n.next
        return n.val

    def is_empty(self):
        return self.head.next==None


class graph:

    def __init__(self,size):
        self.m=[[0]*size for i in range(size)]  # macierz sasiedztwa
    
    def add_edge(self,v,u):
        self.m[v][u]=1

    


# wrzucamy do kolejki pierwszy v, nastepnie wszystkie z nim polaczone ktore
# jeszcze nie byly odwiedzone, wyrzucamy pierwszy i tak postepujemy az wszystkie
# wierzcholki beda odwiedzone - kolejka pusta

def BFS(g,s):  # przekazujemy startowy wiercholek
    
    q=queue()
    number=len(g.m)
    
    # tworzymy pomocnicza tablice czy odwiedzony
    visited=[False]*number

    # tablica na rodzicow
    parents=[None]*number

    # tablica na najkrotsza sciezke od s do v
    dist=[0]*number

    q.enqueue(s)  
    visited[s]=True

    while(not q.is_empty()):
        u=q.dequeue()
        #przegladamy wszystkie wierzcholki polaczone z u
        for i in range(number):
            if q.is_empty() : q=queue()
            if(g.m[u][i]==1 and visited[i]==False) :   # jezeli istnieje krawedz
                parents[i]=u
                visited[i]=True
                dist[i]=dist[u]+1
                q.enqueue(i)
                
    return dist,visited,parents

g=graph(5)
g.add_edge(1,2)
g.add_edge(2,0)
g.add_edge(2,3)
g.add_edge(1,3)
g.add_edge(0,1)
g.add_edge(3,4)
g.add_edge(4,0)

print(BFS(g,0))
