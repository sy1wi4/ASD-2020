'''
Dana jest nieposortowana tablica A[1. . . n] oraz liczba x. Proszę podać algorytm sprawdzający
czy istnieją indeksy i oraz j, takie że A[i] + A[j] = x.
'''

# ALGORYTM: 
'''
Wykorzystujemy słownik (na początek pusty), do którego mamy odstep w czasie stałym.
Iterujemy po wejściowej tablicy i sprawdzamy czy w słowniku jest element, który w sumie
z aktualnym A[i] dałby x. Jeśli tak - kończymy, natomiast jeżeli nie, to dodajemy do słownika
A[i] i powtarzamy algorytm.
'''

def find_pair(arr,x):
    s=set()
    for i in range(len(arr)):
        if x-arr[i] in s: return True
        s.add(arr[i])
    return False
