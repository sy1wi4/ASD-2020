'''
Dany jest zbiór przedziałów otwartych A = {(a1, b1), ...,(an, bn)}. Proszę zaproponować algorytm
(bez implementacji), który znajduje taki zbiór X, X ⊆ {1, ..., n} że:

(a) |X| = k (gdzie k ∈ N to dany parametr wejściowy),

(b) dla każdych i, j ∈ X, przedziały (ai, bi) oraz (aj, bj ) nie nachodzą na siebie

(c) wartość max bj − min ai jest minimalna. 

Jeśli podzbioru spełniającego warunki (a) i (b) nie ma, to algorytm powinien to stwierdzić. 
Algorytm powinien być możliwie jak najszybszy (ale przede wszystkim poprawny).
'''

# ALGORYTM:

'''
1.
Sortujemy przedziały po początkach.
Dla każdego z n przedziałów dokładamy zachłannie jego poprzedników, tak by spełniały warunki zadania i zaczynały się jak
najpóźniej. Wybieramy ten przedział, dla którego max bj - min ai jest minimalne.

O(nlogn+n*k)  -> sprawdzenie dla każdego z n przedziałów k jego poprzedników + posortowanie po końcach

'''
