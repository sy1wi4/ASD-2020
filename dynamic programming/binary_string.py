'''
Dostajemy liczbę naturalną n. Naszym zadaniem jest policzenie wszystkich binarnych (0/1) string'ów
długości n bez jedynek obok siebie.
'''

# ALGORYTM:
'''
Rozważmy osobno liczbę stringów kończących się na 0 oraz na 1 -> dwie tablice.
W tablicach pod indeksem i znajduje się liczba stringów długości i, spełniających
założenia. Zaczynamy uzupełniać tablice od początku - bierzemy coraz dłuższe stringi
"dokładając" 0 lub 1 na koniec. Dzięki temu, że osobno rozważamy przypadki, gdy na końcu 
jest 0 lub 1, to w łatwy sposób możemy stwierdzić, że gdy string aktualnie kończy się na 0,
to możemy dołożyć 0 lub 1, a gdy kończy się on na 1, to dołożyć możemy tylko 0 (1 nie spełnia
założeń). Szukamy sumy ostatnich elementów obu tablic (indeks n).
'''


def count(n):
    zeros=[0]*(n+1)
    ones=[0]*(n+1)

    # jeden bit - 2 możliwości - 0 lub 1
    zeros[1] = 1
    ones[1] = 1

    for i in range(2,n+1):
        # (w nawiasie to co dokładamy w danym kroku)
        zeros[i] += zeros[i-1]   # ...0(0)
        ones[i] += zeros[i-1]    # ...0(1)
        zeros[i] += ones[i-1]    # ... 1(0)
    
    return zeros[n] + ones[n]
