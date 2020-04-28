# ALGORYTM BELLMANA-FORDA znajduje najkrótszą ścieżkę w grafie, dopuszcza ujemne
# wagi krawędzi

# graf nie zawiera ujemnego cyklu, czyli cyklu, w którym suma wag krawędzi jest ujemna
# jeśli tak się stanie zwracamy False

# wykonujemy relaksację wszystkich krawędzi |V|-1 razy, bo taką długość może mieć
# najdłuższa ścieżka w grafie

# następnie weryfikujemy - czy nie ma ujemnego cyklu (jeśli jest, to zapętlilibyśmy się
# w nieskończoność ciągle zmniejszając długość najkrótszej ścieżki)

# O(VE) 


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


# relaksacja krawędzi z u do v
# u to nr wierchołka, v to krotka (wierchołek, waga krawędzi z u do tego wierchołka)
def relax(u,v,parent,distance) :
    
    if distance[v[0]]>distance[u]+v[1] :
        distance[v[0]]=distance[u]+v[1]
        parent[v[0]]=u


# weryfikacja krawędzi z u do v
def verify(u,v,distance) :
    if distance[v[0]]>distance[u]+v[1] : return False
    return True


def bellman_ford(g,s) :
    distance=[float("inf")]*g.size
    distance[s]=0
    parents=[None]*g.size

    for _ in range(g.size-1):
        # przeglądamy wszystkie krawędzi - listy adjacencji każdego z wierchołków
        for vertex in range(g.size) :
            
            for v in range(len(g.arr[vertex])) :
                relax(vertex,g.arr[vertex][v],parents,distance)

    for vertex in range(g.size) :
        
            for v in range(len(g.arr[vertex])) :
                
                if not verify(vertex,g.arr[vertex][v],distance): return False
    
    return distance,parents
