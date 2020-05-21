'''
Zaproponuj strukturę danych udostępniającą następujący interfejs:

    init(length) -tworzy strukturę tablico-podobną o długości length,
    set(index, val) -podstawia pod index wartość val,
    snap() -tworzy snapa struktury i zwraca snap_id, identyfikujący aktualny snap -jest równy liczbie wykonanych do tej pory snapów,
    get(index, snap_id) -zwraca wartość jaka znajdowała się pod index wtedy gdy wywołana funkcja snap zwróciła snap_id.

Wszystkie operacje powinny być jak najszybsze.
'''

# ALGORYTM:
'''
W tablicy długości length trzymamy drzewa (czerwono - czarne). Na początek w każdej komórce jest
tylko root z kluczem 0 i wartością, jaką pod tym samym indeksem aktualnie mamy w wejściowej tablicy.
Trzymamy także informację, ile do tej pory było snapów (na początku 0, więc każde drzewo w roocie ma klucz 0)
Przy wywołaniu set - podstawiamy wartość val pod index w oryginalnej tablicy i do danego drzewa wstawiamy node'a
o kluczu jako aktualny numer snapa oraz wartości, którą dodaliśmy. Dzięki temu przy wywołaniu funkcji get 
wystarczy, że w danym drzewie w tablicy pod indeksem index wyszukamy element o największym kluczu, który 
jest <= od snap_id z funkcji get(index,snap_id). Dzięki temu, jeżeli np wywołamy get(2,5), czyli chcemy 
wiedzieć jaka wartość w tablicy była pod indeksem 2, gdy zrobiona snapa nr 5, to jeżeli wartość w tej komórce
zmieniła się tylko po 2 snapie, a potem już nie, to wystarczy, że znajdziemy to co jest w drzewie pod kluczem 2.
Tak więc operacja get ma złożoność logn - find w drzewie czerwono czarnym. Snap oczywiście to O(n), bo
musimy skopiować tablicę
'''
