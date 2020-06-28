# szukanie cyklu Eulera w grafie (spójnym!)

# DFS, z tą różnicą, że odznaczamy krawędzi, po których przeszliśmy (a nie wierzchołki)
# gdy odwiedzimy już wszystkich sąsiadów danego wierzchołka, to dodajemy go do cyklu

# oznaczamy krawędzie jako odwiedzone wpsiując 2 zamiast 1 w oryginalnym grafie
def cycle(G):
    order=[]
    def DFSvisit(u):      # jestesmy w wierzcholku u

        for v in range(len(G)) :    # idziemy po wszystkich sasiadach
            if G[u][v] == 1:        # gdy istnieje krawędź z u do v i jest ona nieodwiedzona
                G[u][v]=G[v][u]=2
                DFSvisit(v)
        order.append(u)
                
   
    # graf jest nieskierowany oraz spójny, więc po 1 wywołaniu cały graf zostanie odwiedzony 
    DFSvisit(0)
    return order


# macierzowa reprezentacja grafu
arr=  [ [0,1,0,0,0,1],
        [1,0,1,1,0,1],
        [0,1,0,1,0,0],
        [0,1,1,0,1,1],
        [0,0,0,1,0,1],
        [1,1,0,1,1,0] ]

print(cycle(arr))
