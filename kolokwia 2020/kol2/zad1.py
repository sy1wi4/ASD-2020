'''
Proszę zaimplementować funkcję heavypath(T), która na wejściu otrzymuje drzewo T z ważonymi krawędziami 
(wagi to liczby całkowite - mogą być zarówno dodatnie, ujemne, jak i o wartości zero) i zwraca długość (wagę) 
najdłuższej ścieżki prostej w tym drzewie. Drzewo reprezentowane jest za pomocą obiektów typu Node (poniżej).
'''

# ALGORYTM:
'''
Długość najdłuższej ścieżki prostej w drzewie zaczepionym w danym węźle to suma dwóch najdłuższych ścieżek
idących w dół drzewa, chyba, że któraś z nich jest ujemna, to oczywiście jej nie bierzemy. Wynik końcowy 
uzyskujemy rekurencyjnie zagłębiając się w drzewo i obliczając za każdym razem dwie najdłuższe ścieżki. 
Dodatkowo przetrzymujemy długość najdłuższej do tej pory uzyskanej ścieżki. 


'''

class Node:
    def __init__( self ):

        self.child = [] # lista par (dziecko, waga krawędzi)


longest_path = 0

def heavy_path(T):
    
    def path_len(T): 

        global longest_path

        # przetrzymujemy dwie najdłuższe ścieżki w dół
        first = 0 
        second = 0

        for child,weight in T.child :
            
            # długość aktualnej ścieżki w dół
            current_len = path_len(child) + weight 
            
            if current_len > first :
                second = first
                first = current_len
            
            elif current_len > second :
                second = current_len
            
           

        if first + second > longest_path :
            # najdłuższa dotychczas ścieżka prosta w drzewie
            longest_path = first + second
        
        # zwracamy długość najdłuższej ścieżki idącej w dół drzewa
        return first

    path_len(T)
    return longest_path



A = Node()
B = Node()
C = Node()
D = Node()
E = Node()
F = Node()
G = Node()


A.child = [ (B,5), (C,-1) ]
B.child = [ (D,1)]
C.child = [ (E,-2), (F,3) ]
D.child = [ (G,-2)]
print(heavy_path(A))
