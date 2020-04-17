''' Dany jest ciąg przedziałów postaci [ai, bi]. Dwa przedziały można
skleić jeśli mają dokładnie jeden punkt wspólny. Proszę wskazać algorytm dla następującego problemu:

1. Problem stwierdzenia, czy da się uzyskąć przedział [a, b] przez sklejanie odcinków.
'''

class graph:

    def __init__(self,size):
        self.m=[[0]*size for i in range(size)]  # macierz sasiedztwa
    
    def add_edge(self,v,u):
        self.m[v][u]=1

    def print_graph(self):
        printArray(self.m)

def stick(arr,a,b):
    # tworzymy graf z ciagu przedzialow
    # zalozmy ze przedzialy posortowane po koncach,
    # jesli nie, to tworzymy macierz wielkosci najdalszego konca oddcinka
    
    g=graph(arr[len(arr)-1][1]+1)

    for section in arr :
        g.add_edge(section[0],section[1])
    g.print_graph()

    # wywolujemy DFSa z wierzcholka a i sprawdzamy czy odwiedzi od wiercholek b
    #  - jesli tak, to da sie tak posklejac odcinki, by uzyskac przedzial [a,b]

    def DFS(g):
        visited=[False]*len(g.m)

        def DFSvisit(u):
            visited[u]=True
            for i in range(len(g.m)) :
                if g.m[u][i]==1 and not visited[i]:
                    visited[i]=True
                    DFSvisit(i)   
        
        DFSvisit(a)
        return visited[b]
    return DFS(g)
    
    

arr=[[1,3],[2,4],[3,5],[5,7],[6,8],[7,9]]
print(stick(arr,3,7))
