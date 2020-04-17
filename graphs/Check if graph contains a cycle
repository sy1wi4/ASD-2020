# Sprawdzanie czy graf nieskierowany posiada cykl.

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
    
# zmodyfikowany DFS

def cycle(g):

    def has_cycle(g,u):
        visited[u]=True
        for i in g.arr[u][1:] :
            if not visited[i] :
                parent[i]=u
                visited[i]=True
                if has_cycle(g,i) : return True

            else: 
                # sprawdzamy czy sasiad aktualnego, ktory byl juz odwiedzony
                #  jest jest jego rodzicem - jesli nie, tzn ze mamy cykl 
                if parent[u]!=i :
                    return True
        return False
                

    visited=[False]*len(g.arr)
    parent=[None]*len(g.arr)
    
    for i in range(len(g.arr)):
        if not visited[i]:
            if has_cycle(g,i) : return True,parent
    return False


g=graph(4)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(1,3)
g.add_edge(1,0)
g.add_edge(2,1)
g.add_edge(3,2)
g.add_edge(3,1)

g.printG()
print(cycle(g))
