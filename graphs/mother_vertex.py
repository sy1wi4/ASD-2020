# reprezentacja przez listy adjacencji
class graph:
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
    finish=[None]*g.size    # czas przetorzenia wierzchołka

    def DFSvisit(u):      
        global time    
        visited[u]=True
    
        for i in range(1,len(g.arr[u])) :    
            
            ngh=g.arr[u][i]

            if not visited[ngh] :

                visited[ngh]=True
                DFSvisit(ngh)
        
        time+=1
        finish[u]=time

    
    for v in range(g.size):
        
        if not visited[g.arr[v][0]] : 
            DFSvisit(g.arr[v][0])

    # szukamy największego czasu w tablicy finish
    for i in range(len(finish)) :
        
        if finish[i]==len(finish) :
            
            # spr czy dojdziemy do każdego wierzchołka
            visited=[False]*len(finish)
            visited[i]=True
            DFSvisit(i)
            for j in range(len(finish)):
                if visited[j]==False: return False
            return True,i
