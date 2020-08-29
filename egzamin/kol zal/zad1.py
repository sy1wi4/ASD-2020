'''
Dana  jest  tablica  dwuwymiarowa G,  przedstawiająca  macierz  sąsiedztwa  skierowanego  grafu  ważonego, który odpowiada 
mapie drogowej (wagi przedstawiają odległości, liczba -1 oznacza brak krawędzi). W niektórych wierzchołkach są stacje paliw, 
podana jest ich lista P. Pełnego baku wystarczy na przejechanie odległości d. Wjeżdżając na stację samochód zawsze jest tankowany 
do pełna. Proszę  zaimplementować  funkcję jak dojade(G, P, d, a, b),  która  szuka  najkrótszej  możliwej trasy od wierzchołka 
a do wierzchołka b, jeśli taka istnieje i zwraca listę kolejnych odwiedzanych na trasie wierzchołków (zakładamy, że w a też 
jest stacja paliw; samochód może przejechać najwyżej odległość d bez tankowania).
'''
# ALGORYTM:
'''
Wykorzystujemy algorytm Floyda-Warshalla, by znaleźć najkrótsze ścieżki między stacjami, następnie na podstawie
uzyskanej macierzy odległości zostawiamy tylko wierzchołki a i b oraz stacje i usuwamy krawędzi (najkrótsze ścieżki
między danymi wierzchołkami wliczone uprzednio) o długości większej niż d, bo przez nie nie zdołamy przejechać. 
Następnie używamy jakiegoś algorytmu do wyznaczenia najkrótszej ścieżki od a do b, np. ponownie Floyda-Warschalla. 
'''

def floyd_warshall(g):

    n = len(g)

    # tworzymy macierz odległości, gdzie dist[u][v] to długość najkrótszej ścieżki z u do v
    dist=[[None]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dist[i][j]=g[i][j]
    
    # tablica parentów, gdzie parent[u][v] oznacza poprzednika v na ścieżce z u do v
    parents=[[None]*n for _ in range(n)]

    # tam, gdzie jest krawędź między wierzchołkami wpisujemy jej wagę, jeśli nie ma - inf, na przekątnej 0
    for i in range(n):
        for j in range(n):
            if dist[i][j]==-1: 
                if i!=j :
                    dist[i][j]=float("inf")
                else:
                    dist[i][j]=0

    
    for i in range(n):
        for j in range(n): 
            
            if g[i][j] != 0 : parents[i][j]=i  
            
    
    # sprawdzamy, czy scieżka z u do v jest krótsza z wykorzystaniem wierzchołka s czy nie
    for s in range(n) :
        for u in range(n) :
            for v in range(n) :
                if dist[u][s]+dist[s][v] < dist[u][v]:
                    dist[u][v]=dist[u][s]+dist[s][v]
                    parents[u][v]=parents[s][v]

    return dist,parents







def jak_dojade(G, P, d, a, b) :

    new_g, parents = floyd_warshall(G)
  
    # dla ułatwienia oznaczmy w których wierzchołkach są stacje
    station=[False]*len(G)
    for i in range(len(P)):
        station[P[i]] = True
    
    # "usuwamy" z grafu wierzchołki niebędące a, b ani stacją, a także krawędzi dłuższe niż d

    for row in range(len(G)) : 
        for col in range(len(G)) :
           
            if not station[row] or not station[col] or new_g[row][col] > d :
               
                if new_g[row][col] <= d and col == b :
                    pass

                else:
                    new_g[row][col] = -1


    dist,new_parents = floyd_warshall(new_g)
    
    length = dist[a][b]
    
    # pomocnicza funckja do odtwarzania ścieżki na podstawie macierzy rodziców
    # uzyskanej po uruchomieniu algorytmu Floyda - Warshalla

    def create_path(path,u,v):
        current_parent=parents[u][v]
        last=v  # ostatni na rozważanej ścieżce
        current_parent = parents[u][v]

        while current_parent != u :
            path.append(last)
            last=current_parent
            current_parent = parents[u][last]
        path.append(last)
        


    if length == float("inf") :
        return None
    
    else:
        # zwracamy ścieżkę
        path=[]

        cur_last = b
        cur_parent = new_parents[a][b]

        while cur_parent != a :
            create_path(path,cur_parent,cur_last)
            cur_last = cur_parent
            cur_parent = new_parents[a][cur_last]
        
        create_path(path,a,cur_last)

        path.append(a)
        
        # mamy ścieżkę w odwróconej kolejności

        return path[::-1]
