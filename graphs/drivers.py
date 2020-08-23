'''
Dana jest mapa kraju w postaci grafu G = (V, E), gdzie wierzchołki to miasta a krawędzie to drogi 
łączące miasta. Dla każdej drogi znana jest jej długość (wyrażona w kilometrach jako liczba naturalna). 
Alicja i Bob prowadzą (na zmianę) autobus z miasta x∈V do miasta y∈V, zamieniając się za kierownicą w 
każdym kolejnym mieście. Alicja wybiera trasę oraz decyduje, kto prowadzi pierwszy. Proszę zaproponować algorytm, 
który wskazuje taką trasę (oraz osobę, która ma prowadzić pierwsza), żeby Alicja przejechała jak najmniej kilometrów. 
Algorytm powinien być jak najszybszy (ale przede wszystkim poprawny).
'''

# ALGORYTM:

'''
Dany graf modyfikujemy tak, że każdy wierzchołek rozbijamy na dwa (dla Alicji i Boba).
Każda istniejąca krawędź z u do v staje się teraz dwiema - łączy  wierzchołki uA-vB oraz
uB-vA. Pierwsza oznacza, że jedzie Alicja, druga, że Bob. Ponieważ chcemy zminimalizować wagi
krawędzi, po których jedzie Alicja, to krawędź uA-vB ma wagę jak oryginalna krawędź, natomiast 
uB-vA ma wagę 0 (bo nie interesuje nas Bob). Puszczamy algorytm Dijkstry z wierzchołka xA oraz
z xB i sprawdzamy, która ścieżka do y jest krótsza - tę wybieramy.
'''

# ZŁOŻONOŚĆ: 0(V^2)   -> 2 razy algorytm Dijkstry po grafie o V wierzchołkach (na macierzy)


# reprezentacja listowa - graf nieskierowany
class Graph:
    def __init__(self,size):
        self.size=size
        self.arr=[[] for _ in range(size)]

    def add_edge(self,v,u,weight): # krawedz z v do u
        self.arr[v].append([u,weight])      # tworzymy krotki (u,waga krawedzi z v do u)
   

    def printG(self):
        print("\n")
        v=0
        for i in self.arr:
            print(v,i)
            v+=1
            print("\n")


from queue import PriorityQueue

def dijkstra(g,s):
    p=PriorityQueue()

    # dodaje do kolejki wszystkie wierzcholki w postaci krotek (waga,u)
    for i in range(g.size) :
        p.put((float("inf"),i))
    
    parents=[None]*g.size

    # na początku odległości wszędzie to inf, na bieżąco będę aktualizować
    distance=[float("inf")]*g.size
    distance[s]=0
    
    while not p.empty() :
        u=p.get()       # dostaje krotke (odleglosc,wierzcholek)
        

        for i in range(len(g.arr[u[1]])) :
            ngh=g.arr[u[1]][i]      # lista 2-elementowa [wierzcholek, waga]

            #relaksacja
            if distance[ngh[0]] > distance[u[1]]+ngh[1] :
                distance[ngh[0]] = distance[u[1]]+ngh[1]
                p.put((distance[ngh[0]],ngh[0]))
                
                parents[ngh[0]]=u[1]

    return distance


def drivers(g,x,y):

    # tworzymy nowy graf, w którym wierzchołkowi u z oryginalnego odpowiadają wierzchołki
    # 2*i (dla Alicji) oraz 2*i+1 (dla Boba)

    new_g=Graph(2*g.size)

   # dodajemy odpowiednie wierzchołki uA-vB z oryginalną wagą oraz uB-vA w wagą 0
    for i in range(g.size) :
        for j in range(len(g.arr[i])) :
            
            new_g.add_edge(2*i,g.arr[i][j][0]*2+1,g.arr[i][j][1])
            new_g.add_edge(2*i+1,g.arr[i][j][0]*2,0)




    # odległości do poszczególnych gdy pierwsza jedzie Alicja (A) lub Bob (B)
    A = dijkstra(new_g,2*x)
    B = dijkstra(new_g,2*x+1)

    Alice_first = min(A[2*y],A[2*y+1])
    Bob_first = min(B[2*y],B[2*y+1])

    if Alice_first < Bob_first :
        print("Alice first")
        return Alice_first
    
    else :
        print("Bob first")
        return Bob_first

    


g=Graph(4)
g.add_edge(0,1,3)
g.add_edge(0,2,8)
g.add_edge(2,3,3)
g.add_edge(1,3,4)
g.add_edge(1,2,5)
g.printG()

print(drivers(g,0,3))
