'''
Mamy dany graf skierowany G= (V, E) oraz funkcję opisującą przepustowość każdej krawędzi (liczbę jednostek towaru na godzinę, 
które mogą się przemieszczać krawędzią). Poza tym mamy dany zbiór wierzchołków - fabryk S = {s1, . . . , sn}
oraz zbiór wierzchołków - sklepów T = {t1, . . . , tm}. Dla każdej fabryki znamy liczbę określającą ile jednostek towaru 
na godzinę fabryka może maksymalnie produkować. Jednocześnie dla każdego sklepu mamy liczbę, która mówi, ile jednostek 
towaru na godzinę musi do tego sklepu docierać. Proszę podać algorytm, który sprawdza, czy da się zapewnić, żeby do każdego 
sklepu docierało z fabryk dokładnie tyle jednostek towaru ile sklep wymaga jednocześnie nie zmuszając żadnej fabryki do 
przekroczenia swoich możliwości produkcyjnych i nie przekraczając przepustowości żadnej z krawędzi.
'''

# ALGORYTM:
''' 
Tworzymy super-źródło oraz super-ujście, gdzie przepustowościami są odpowiednio max ilość towaru, jaką może wyprodukowac fabryka
oraz ilość towaru, jakiej wymagają poszczególne sklepy. Następnie wykorzystujemy algorytm do znalezienia max przepływu w tym grafie
i sprawdzamy, czy każda krawędź ze sklepu do ujścia jest maksymalnie obciążona - tj. czy da się dostarczyć całe zapotrzebowanie.
'''

class graph:

    def __init__(self,size):
        self.m=[[0]*size for i in range(size)] 
        self.size=size
    
    def add_edge(self,v,u,weight):
        self.m[v][u]=weight
    
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

def check(g,factories,stores):
    
    # aby dodać superwierzchołki tworzymy nową macierz, gdzie sklepy mają indeks len(matrix)-2,
    # a fabryki len(matrix-1)
    matrix=[[0]*(len(g.m)+2) for _ in range(len(g.m)+2)]
    for i in range(len(g.m)):
        for j in range(len(g.m)):
            matrix[i][j]=g.m[i][j]
    
    f=len(matrix)-2
    s=len(matrix)-1

    # dodajemy krawędzi z super-źródła do fabryk
    for factory,weight in factories:
        matrix[f][factory]=weight
    
    # dodajemy krawędzi ze sklepów do super-ujścia
    for store,weight in stores:
        matrix[store][s]=weight
    
    for i in matrix:
        print(i)
    
    flow=Ford_Fulkerson(matrix,f,s)
    print(flow)

    # sprawdzamy czy każda krawędź z fabryki do super-ujścia została pokryta maksymalnie dane przez flow,
    # czyli czy suma wag krawędzi  == flow

    Sum=0
    for i in range(len(stores)):
        Sum += stores[i][1] 
    
    return Sum == flow


g=graph(6)
g.add_edge(0,1,16)
g.add_edge(1,3,12)
g.add_edge(3,5,20)
g.add_edge(4,5,4)
g.add_edge(2,4,14)
g.add_edge(0,2,13)
g.add_edge(3,2,9)
g.add_edge(2,1,4)
g.add_edge(1,2,10)
g.add_edge(4,3,7)

# fabryki reprezentowane jako krotki (nr wierzchołka, max ilość jaką może wyprodukować)
factories=[(0,12),(1,10)]

# sklepy reprezentowane jako krotki (nr wierzchołka, ilość jaka musi być dostarczona)
stores=[(4,8),(5,10)]


check(g,factories,stores)
