# ALGORYTM DIJKSTRY znajduje najkrótszą ścieżkę w grafie o nieujemnych wagach

# O(ElogV)

from queue import PriorityQueue

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


def dijkstra(g,s):
    p=PriorityQueue()

    # dodaje do kolejki wszystkie wiercholki w postaci krotek (waga,u)
    for i in range(g.size) :
        p.put((float("inf"),i))
    
    parents=[None]*g.size

    # na początku odległości wszędzie to inf, na bieżąco będę aktualizować
    distance=[float("inf")]*g.size
    distance[s]=0
    
    while not p.empty() :
        u=p.get()       # dostaje krotke (odleglosc,wierzcholek)
        print(u)
        print("x",len(g.arr[u[1]]))

        for i in range(len(g.arr[u[1]])) :
            ngh=g.arr[u[1]][i]      # lista 2-elementowa [wierzcholek, waga]

            #relaksacja
            if distance[ngh[0]] > distance[u[1]]+ngh[1] :
                distance[ngh[0]] = distance[u[1]]+ngh[1]
                p.put((distance[ngh[0]],ngh[0]))
                
                parents[ngh[0]]=u[1]
    return distance,parents
