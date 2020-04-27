# szukamy najkrótszej ścieżki z u do v w grafie ważonym, tworząc wirtualnie "dodatkowe wierchołki"
# na danej krawędzi (ich liczba jest o 1 mniejsza od wagi krawędzi) - dzięki temu mamy graf nieważony 
# i możemy użyć BFS-a 

# reprezentacja przez listy sąsiedztwa
class Graph:
    def __init__(self,size):
        self.size=size
        self.arr=[[] for _ in range(size)]

    def add_edge(self,v,u,weight): # krawedz z v do u
        self.arr[v].append((u,weight))      # tworzymy krotki (u,waga krawedzi z v do u)

    def printG(self):
        print("\n")
        v=0
        for i in self.arr:
            print(v,i)
            v+=1
            print("\n")


class node:
    def __init__(self):
        self.val=None
        self.next=None

class queue:
    def __init__(self):
        self.head=node()
        self.tail=node()
    
    def put(self,x):    
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
    
    def get(self):     
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


def BFS(g,u) :
    # każdy oryginalny wierzchołek ma postać (u,0,rodzic,waga kraw)
    # wierchołki "sztuczne mają postać" (u,długość krawędzi-1,rodzic, waga kraw)
    # gdy ściągamy wierzchołek "sztuczny" z kolejki, to od razu do
    # kolejki dodajemy krotkę z drugim elementem mniejszym o 1

    q=queue()
    size=g.size

    visited=[False]*size
    distance=[0]*size

    q.put((u,0,None,0))  # początkowy wierzchołek
    visited[u]=True

    while not q.is_empty() :
        v=q.get()   # otrzymujemy krotkę (u,ktory,rodzic,waga kraw)
        
        if q.is_empty() : q=queue()
        
        # gdy sciagniemy w kolejki wiercholek sztuczny, to dodaje do kolejki nastepny
        if v[1] != 0 :
            
            q.put(( v[0], v[1]-1,v[2],v[3] ))
            
            print("dodany",v)

        # gdy sciagniemy z kolejki wiercholek oryginalny i nie byl on odwiedzony, to wpisujemy mu odleglosc rodzica + waga krawedzi miedzy nimi
        else :
            
            if not visited[v[0]]:
                visited[v[0]] = True
                if v[2] is not None: distance[v[0]]=distance[v[2]]+v[3]
                else: distance[v[0]]=v[3]

            for i in range(len(g.arr[v[0]])) :

                ngh=g.arr[v[0]][i][0]
                weight=g.arr[v[0]][i][1]
                
                if not visited[ngh] :
                    q.put((ngh,weight-1,v[0],weight))
        
 
    return distance
