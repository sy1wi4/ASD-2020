'''
Ścieżka  Hamiltona  to  ścieżka  przechodząca  przez  wszystkie  wierzchołki w grafie, przez każdy dokładnie raz.
W ogólnym grafie znalezienie ścieżki Hamiltona jest problememNP-trudnym. Proszę podać algorytm, który stwierdzi
czy istnieje ścieżka Hamiltona w acyklicznym grafie skierowanym.
'''

# musimy posortować wierzchołki topologicznie i sprawdzić, czy między każdymi kolejnymi istnieje ścieżka

# sprawdza czy istnieje krawędź z u do v
def find_edge(u,v):
    for vertex in G[u]:
        if vertex==v :
            return True 
            
    return False 

flag=True

def path(G):
    
    order=[]

    def DFSvisit(u):     
        global flag

        visited[u]=True
        for i in range(len(G[u])) :    
            
            ngh=G[u][i]   

            if not visited[ngh] :
                DFSvisit(ngh)
        
        order.append(u)

        if len(order) > 1:
            if not find_edge(u,order[len(order)-2]) : 
                print("no edge between",u,"and",order[len(order)-2])
                flag=False
        
    
    # lista order jest w odwrotnej kolejności, na bieżąco sprawdzam, 
    # czy istnieje ścieżka z dodanego wierzchołka do poprzedzającego 
    # go na tej liście (czyli w dobrej kolejności będącego "po nim")

    
    visited=[False]*len(G)

    for v in range(len(G)):
        if not visited[v] : 
           DFSvisit(v)
           if not flag:
                return False
            
    return True,order[::-1]
   

# reprezentacja przez listy sasiedztwa
G=[[1],[3],[4],[2,4],[]]
print()
print(path(G))
