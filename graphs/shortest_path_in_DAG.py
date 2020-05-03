'''
Jak znaleźć najkrótsze ścieżki z wierzchołka s do wszystkich innych 
w acyklicznym grafie skierowanym? (Krawędzie są ważone.)
'''

# ALGORYTM 
# O(V+E)

# sortujemy topologicznie wierzchołki, na początku ścieżki do każdego wierzchołka 
# mają długość inf, do s 0, następnie dla kolejnych posortowanych wierzchołków (u), 
# zaczynając od s (wierzchołków poprzedzających s nie musimy brać pod 
# uwagę, ponieważ z definicji sortowania topologicznego wiemy, że nie istnieje
# do nich żadna ścieżka z s) przeglądamy ich sąsiadów (v) i dla każdego z nich wykonujemy 
# algorytm relaksacji krawędzi z u do v
# w rezultacie otrzymamy najkrósze ścieżki do każdego wierzchołka osiągalnego z s
