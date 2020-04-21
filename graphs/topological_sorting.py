def DFS(G):
    
    # kolejność w odwróconym porzadku
    order=[]

    def DFSvisit(u):      # jestesmy w wierzcholku u
        
        visited[u]=True
        for i in range(len(G[u])) :    # idziemy po wszystkich sasiadach
            # i to indeks sasiada u
            ngh=G[u][i]   # aktualny sasiad

            if not visited[ngh] :

                DFSvisit(ngh)
        
        order.append(u)
    
    # wywolujemy z kazdego wierzcholka funkcje DFSvisit, 
    # bo za jednym razem mozemy nie przejsc calego grafu
    
    visited=[False]*len(G)
    for v in range(len(G)):
        
        if not visited[v] : 
            DFSvisit(v)

   # zwracamy kolejnosc posortowanych wierzcholkow 
    return order[::-1]   


# reprezentacja przez listy sasiedztwa
G=[[1,2,4],[2,3],[],[5,6],[3],[],[]]
print(DFS(G))
