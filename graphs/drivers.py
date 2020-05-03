'''
Dana jest mapa kraju w postaci grafu G=(V, E), gdzie wierzchołki to miasta a krawędzie to drogi 
łączące miasta. Dla każdej drogi znana jest jej długość (wyrażona w kilometrach jako liczba naturalna). 
Alicja i Bob prowadzą (na zmianę) autobus z miasta x∈V do miasta y∈V, zamieniając się za kierownicą w 
każdym kolejnym mieście. Alicja wybiera trasę oraz decyduje, kto prowadzi pierwszy. Proszę zapropnować algorytm, 
który wskazuje taką trasę (oraz osobę, która ma prowadzić pierwsza), żeby Alicja przejechała jak najmniej kilometrów. 
Algorytm powinien być jak najszybszy (ale przede wszystkim poprawny).
'''

# ALGORYTM:

# Każde miasto "rozbijamy" na 2 - dla Boba i dla Alicji. Jeżeli jedzie Alicja, to dodajemy jej
# wagę krawędzi a Bobowi - 0, analogicznie gdy jedzie Bob. Na tak zmodyfikowanym grafie uruchamiamy
# algorytm Dijkstry - znajdzie on szukaną trasę i rozpoczynającą osobę.
