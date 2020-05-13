'''
Dany jest zbiór punktów X={x1, . . . , xn} na prostej. Proszę podać algorytm, który znajduje minimalną liczbę
przedziałów jednostkowych domkniętych, potrzebnych do pokrycia wszystkich punktów z X. 
(Przykład: JeśliX={0.25,0.5,1.6}to potrzeba dwóch przedziałów, np. [0.2,1.2] oraz [1.4,2.4]).
'''

# ALGORYTM:

'''
Jeżeli punkty nie są posortowane w porządku rosnącym, to zaczynamy od posortowania ich. Następnie
wybieramy pierwszy przedział [x1,x1+1], który pokryje pierwszy punkt i wszystkie kolejne oddalone
o maksymalnie 1 od danego (w prawo). Powtarzamy to samo dla następnego punktu, który jest dalej
niż x1+1. Kończymy wraz z dojściem do najdalszego punktu.
'''

# ZŁOŻONOŚĆ: O(n)  ( + O(nlogn)->jeżeli nieposortowane ) = O(nlogn)
