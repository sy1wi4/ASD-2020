'''
    Wiemy, że:
    
    1.  korzeń drzewa DFS jest punktem artykulacji wtw gdy ma co najmniej dwoje dzieci
    2.  jeśli v nie jest korzeniem w drzewie DFS, v jest punktem artukulacji wtw
        gdy ma co najmniej jednego syna i dla conajmniej jednego syna nie istnieje krawędź
        wsteczna {x,y} taka,  x - potomek syna, y - przodek x

    ALGORYTM:
    
    Uruchamiamy DFS i obliczamy low (jak w przypadku mostów).
    Jeśli korzeń ma więcej niż jednego syna to jest pkt-em art.
    Jeśli v ma syna takiego, że low(u) >= d(v) (czyli syn v nie laczy sie z czyms nad v
    lub nim samym, a co za tym idzie, usunięcie v nie spowoduje rozspójnienia grafu),
    tzn. że v jest pkt-em art.
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

def points(g):
    visited=[False]*g.size
    parents=[None]*g.size
    entry=[None]*g.size
    low=[None]*g.size
    
    points=[]

    def DFSvisit(u):      
        global time
        time+=1
        entry[u]=time
        low[u]=time
        visited[u]=True

        for i in range(1,len(g.arr[u])) :   
            children=0
            ngh=g.arr[u][i]

            if not visited[ngh] :
                parents[ngh]=u
                children+=1
                visited[ngh]=True
                DFSvisit(ngh)

                # przy powrocie rekurencji  (gdy już odwiedzimy wszystkie
                #  dzieci) sprawdzamy czy poniżej była jakaś krawędź wsteczna 
                low[u]=min(low[u],low[ngh])

                if parents[u] is None and  children >= 2 :
                    # root
                    points.append(u)
        
                elif parents[u] is not None and low[ngh]>=entry[u] :
                    points.append(u)

            
            elif visited[ngh] and parents[u] != ngh :

                # krawędź wsteczna
                low[u]=min(low[u],entry[ngh])
       
    for v in range(g.size):
        
        if not visited[g.arr[v][0]] : 
            DFSvisit(g.arr[v][0])

    return points
