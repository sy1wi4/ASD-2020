'''
Dane są dwa wektory x= (x1, . . . , xn) ∈ N oraz y= (y1, . . . , yn) ∈ N takie, że sumy współrzędnych obu wektorów
są takie same. Pojedyncza operacja przenoszenia powoduje zmniejszenie jednego pola wektora i zwiększenie pola obok 
(ale żadne pole nigdy nie może zmniejszyć się poniżej zera). Odległość Wassersteina tych wektorów — zapisywana jako 
d(x, y) — zdefiniowana jest jako najmniejsza liczba operacji przenoszenia potrzebnych do zamiany wektora x w wektor y. 
(Intuicyjnie wektory opisują, ile kamyczków jest w poszczególnych polach wektora i pojedyncza operacja przenosi jeden 
kamyczek o jedno pole; interesuje nas minimalna liczba ruchów). Proszę zaproponować możliwie jak naszybszy algorytm 
obliczający odległość Wassersteina dwóch wektorów.
'''

# ALGORYTM:
'''
Stosujemy algorytm zachłanny, przesuwając sie po wektorze x i sprawdzając na bieżąco, czy wartość jest za duża
czy za mała (w stosunku do y) i odpowiednio odejmujemy lub dodajemy tak, by się zrównała z wartością z y.
'''

import math

def distance(x,y):
    # zmieniamy wektor x w y
    moves=0
    for i in range(len(x)):
        if x[i] != y[i]:
            moves += abs(x[i]-y[i])
            x[i+1] += x[i]-y[i]
            x[i] = y[i]
    return moves

x = [1,3,2,4]
y = [3,2,2,3]

distance(x,y)
