'''
Dane jest n zmiennych x1, ..., xn, o nieznanych wartościach. Mamy jednak podaną serię równości i różności, 
postaci: xi=xj, xi!=xj. Podaj jak najszybszy algorytm, który sprawdzi, czy podana tak seria nie jest sprzeczna.
'''


# ALGORYTM:

'''
Wykorzystamy find/union. Na początku każda ze zmiennych tworzy osobny zbiór. Przechodzimy po równościach 
i łączymy zbiory do których należą zmienne z danej równości. Następnie przechodzimy po różnościach i sprawdzamy,
czy obie zmienne są w różnych zbiorach - jeżeli nie (są w tym samym), to znaczy że są jednocześnie równe 
i różne - a więc sprzeczność.
'''

# O((n+m)log*(n+m), gdzie m jest liczbą zależności między zmiennymi
