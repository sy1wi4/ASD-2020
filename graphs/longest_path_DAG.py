'''
Podaj jak najszybszy algorytm obliczający najdłuższą ścieżkę w ważonym DAG, startując ze źródła s
'''

# ALGORYTM:
'''
Sortujemy graf topologicznie, następnie w tej kolejności (zaczynając od wierzchołka s 
wykonujemy odwróconą relaksację, powiększając najdłuższą ścieżkę, jeśli to możliwe.
'''


class Graph:
    def __init__(self,size):
        self.size=size
        self.m=[[i] for i in range(size)]

    def add_edge(self,v,u,weight): 
        self.m[v].append((u,weight))

    def printG(self):
        print("\n")
        for i in self.m:
            for j in i:
                print(j,end=" ")
            print("\n")

# sortowanie topologiczne DAG-u
def sort(G):
    
    # kolejność w odwróconym porządku
    order=[]

    def DFSvisit(u):    
        
        visited[u]=True
        for i in range(1,len(g.m[u])) :  
    
            ngh=g.m[u][i][0]  

            if not visited[ngh] :
                DFSvisit(ngh)     
        order.append(u)

    visited=[False]*g.size
    for v in range(g.size):
        
        if not visited[v] : 
            DFSvisit(v)

   # zwracamy kolejnosc posortowanych wierzcholkow 
    return order[::-1] 

# odwrócona relaksacja krawędzi z u do v o wadze weight - możliwie zwiększamy odległość
def relax(u,v,weight,parents,distance):
    if distance[v] < distance[u] + weight :
        distance[v] = distance[u] + weight
        parents[v]=u


def longest_path(g,s):
    sorted_graph=sort(g)
    print(sorted_graph)
    
    distance=[float("-inf")]*g.size
    distance[s]=0
    parents=[None]*g.size

    # zaczynamy relaksować od s, bo wcześniejszych nie ma sensu
    i=0
    while sorted_graph[i] != s :
        i += 1
    
    while (i != len(sorted_graph)):
        u=sorted_graph[i]

        for j in range(1,len(g.m[u])):
            v,weight=g.m[u][j]

            relax(u,v,weight,parents,distance)
        i+=1

    print(distance)
    # zwracamy największą wartość z tablicy distance
    return max(distance)
