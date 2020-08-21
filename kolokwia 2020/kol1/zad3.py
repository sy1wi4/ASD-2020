'''
Proszę zaproponować algorytm, który dla tablicy liczb całkowitych rozstrzyga czy każda liczba z tablicy jest sumą dwóch innych liczb z tablicy. 
Zaproponowany algorytm powinien być możliwie jak najszybszy. Proszę oszacować jego złożoność obliczeniową.

'''


# ALGORYTM:
''' 
    Najpierw posortujmy wejściową tablicę np quick lub merge sortem O(nlogn). Następnie dla każdej liczby z tej tablicy będziemy
    sprawdzać czy istnieje w tablicy para sumująca się do tej zadanej liczby. Możemy takie sprawdzenie wykonać liniowo - 
    zaczynamy z dwoma pomocniczymi indeksami od lewego i prawego końca tablicy i sumując elementy, następnie sprawdzamy jak ta suma
    ma się do naszej szukanej.
    Jeżeli jest mniejsza do zwiększamy lewy indeks, jeśli większa - zmniejszamy prawy, jeżeli zanim indeksy się zrównają, któraś
    z sum będzie tą szukaną - OK, powtarzamy to samo dla kolejnej liczby w tablicy, jeżeli nie - zwracamy False i kończymy algorytm.
    Jeśli przejdziemy całą wejściową, znaczy to, że znaleźliśmy w tablicy pary sumujące się do każdej z liczb - zwracamy True. 
'''

# ZŁOŻONOŚĆ:  O(nlogn + n^2)
# sortujemy i dla każdego z n elementów wyszukujemy liniowo, czy istnieje sumująca się para
