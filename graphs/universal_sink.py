'''
Mówimy,  że  wierzchołek t w  grafie  skierowanym  jest  uniwersalnym ujściem, jeśli 
(a) z każdego innego wierzchołka v istnieje krawędź z v do t 
(b) nie istnieje żadna krawędźwychodząca z t.
Proszę podać algorytm znajdujący ujście (jeśli istnieje) przy reprezentacji macierzowej grafu.
'''

# ALGORYTM:
'''
Zauważmy, że przy reprezentacji macierzowej grafu, gdy rozważamy M[u][v], to jeżeli jej wartość
wynosi 0 - tzn. że krawędzi z u do v nie ma, a co za tym idzie v nie może być uniwersalnym ujściem.
Natomiast taka krawędź istnieje (M[u][v] == 1), to uniwersalnym ujściem nie może być u.
Dzięki tej obserwacji możemy liniowym przejściem znaleźć kandydata na uniwersalne ujście.
Kiedy napotkamy na wartość 0 idziemy "w prawo" (inkrementujemy v), jeżeli na 1, to "w dół".
Kiedy dojdziemy z v poza ostatnią kolumnę, oznacza to tyle, że wierzchołek u 
jest kandydatem - i tylko dla niego sprawdzamy, czy cały u-ty wiersz składa się z 0, 
a cała u-ta kolumna z 1 (z wyjątkiem u-tego elementu). Jeżeli natomiast wyjdziemy z v za
ostatni wiersz, to ujścia nie ma.
'''



class graph:

    def __init__(self,size):
        self.size=size
        self.m=[[0]*size for i in range(size)]  # macierz sąsiedztwa
    
    def add_edge(self,v,u):
        self.m[v][u]=1



def universal_sink(g) :
    u = 0
    v = 0

    while u != g.size and v != g.size :

        if g.m[u][v] == 0 :
            v += 1
        
        else:
            u += 1


    # pomocnicza funkcja sprawdzająca, czy dany wierzchołek jest uniwersalnym ujściem
    def is_sink(u) :
        for v in range(g.size) :
            if g.m[u][v] == 1 :
                return False
            if g.m[v][u] == 0 and u != v :
                return False
        
        return True



    if u == g.size :
        return None


    else :
        # sprawdzamy, czy u-ty wierzchołek jest uniwersalnym ujściem
        if is_sink(u) :
            return u
        else:
            return None
