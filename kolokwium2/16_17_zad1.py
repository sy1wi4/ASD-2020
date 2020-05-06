'''
Dana jest mapa kraju w postaci grafu G = (V, E), gdzie wierzchołki to miasta a krawędzie to
drogi łączące miasta. Dla każdej drogi znana jest jej długość (wyrażona w kilometrach jako liczba
naturalna). Alicja i Bob prowadzą (na zmianę) autobus z miasta x ∈ V do miasta y ∈ V ,
zamieniając się za kierownicą w każdym kolejnym mieście. Alicja wybiera trasę oraz decyduje kto
prowadzi pierwszy. Proszę zaproponować algorytm, który wskazuje taką trasę (oraz osobę, która
ma prowadzić pierwsza), żeby Alicja przejechała jak najmniej kilometrów. Algorytm powinien
być jak najszybszy (ale przede wszystkim poprawny). Proszę oszacować złożoność
zaproponowanego algorytmu, zakładając, że graf jest reprezentowany macierzowo.
'''

# ALGORYTM:

'''
Dany graf modyfikujemy tak, że każdy wierzchołek rozbijamy na dwa (dla Alicji i Boba).
Każda istniejąca krawędź z u do v staje się teraz dwiema - łączy  wierzchołki uA-vB oraz
uB-vA. Pierwsza oznacza, że jedzie Alicja, druga, że Bob. Ponieważ chcemy zminimalizować wagi
krawędzi, po których jedzie Alicja, to krawędź uA-vB ma wagę jak oryginalna krawędź, natomiast 
uB-vA ma wagę 0 (bo nie interesuje nas Bob). Puszczamy algorytm Dijkstry z wierzchołka xA oraz
z xB i sprawdzamy, która ścieżka do y jest krótsza - tę wybieramy.
'''

# ZŁOŻONOŚĆ: 0(V^2)   -> 2 razy algorytm Dijkstry po grafie o V wierzchołkach (na macierzy)
