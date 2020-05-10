'''
W miasteczku są sklepy i domy. Trzeba sprawdzić jak daleko do najbliższego sklepu mają
mieszkańcy.
W każdym wierchołku informacja, czy to sklep, odległość do pozostałych wierzchołków.
Szukamy dla każdego wierzchołka
Zaproponować funkcję distanceToClosestStore(g) obliczającą odległość do najbliższego sklepu i oszacować złożoność algorytmu.
'''
# ALGORYTM:

'''
Tworzymy jeden sztuczny wierchołek, który łaczymy ze wszystkimi sklepami krawędzią
o wadze 0, następnie z tego wierzchołka puszczamy algorytm Dijkstry. Odległości
z niego do poszczególnych domów będą także odległością do najbliższego sklepu.
'''

# ZŁOŻONOŚĆ: O(V+E)
