'''
Jak znaleźć cykl o minimalnej wadze w grafie skierowanym z dodatnimi wagami?
Zakładamy reprezentację macierzową
'''

# ALGORYTM:

# GRAF RZADKI - po kolei "usuwamy" każdą krawędź (u,v), a następnie puszczamy Dijkstrę 
# z u i do odległości jaką otrzymamy dla wierzchołka v dodajemy wagę krawędzi z u do v,
# po przejrzeniu wszystkich krawędzi w ten sposób mamy cykl o minimalnej wadze
# O(E^2 * logV)

# GRAF GĘSTY - dla każdej pary wierzchołków szukamy sumy najkrótszych ścieżek z u do v 
# oraz z v do u, bierzemy najmniejszą sumę
# O(V^3)
