'''
W  pewnym  laboratorium  genetycznym powstał ciąg sekwencji DNA. Każda sekwencja to pewien napis składający 
się z symboli G,A,T,C. Przed dalszymi badaniami konieczne jest upewnić się, że wszystkie sekwencje DNA są parami rózne. 
Proszę opisać algorytm, który sprawdza czy tak faktycznie jest.
'''
# ALGORYTM:
'''
Tworzymy drzewo, gdzie root ma 4 dzieci - odpowiednio G A T C. Dodajemy wszystkie istniejące sekwencje
na bieżąco sprawdzając, czy się nie powtarzają. Osiągniemy to poprzez dodanie do każdego węzła pola
end=False, które ustawiamy na True, gdy w danym węźle kończy się jakaś sekwencja. Dzięki temu dodając 
sekwencję, jeżeli okaże się, że nie musimy wstawiać do drzewa nowego węzła oraz kończy się
ona w węźle dla którego już mamy end=True, tzn, że mamy duplikat.
'''
