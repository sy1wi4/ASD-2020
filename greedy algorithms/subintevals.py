'''Dany jest zbiór przedziałów I={[a1, b1], . . . ,[an, bn]}. Mówimy, że przedział [ai, bi] deaktywuje przedział 
[aj, bj] jeśli pierwszy jest podzbiorem drugiego. Proszę zaproponować algorytm, który znajduje podzbiór I o maksymalnym 
rozmiarze taki, że żaden przedział nie jest deaktywowany przez inny (innymi słowy, należy dany przedział usunąć 
jeśli jest nadzbiorem innego, aspośród identycznych przedziałów usunąć wszystkie poza jednym).
'''

# ALGORYTM:
'''
Sortujemy dane przedziały po początkach. Do algortymu wykorzystamy kolejkę priorytetową, w której umieszczać
będziemy końce poszczególnych przedziałów. Rozważamy kolejne przedziały, jeżeli koniec przedziału jest <= od 
najdalszego końca będącego w kolejce, tzn. że rozważany przedział go deaktywuje. Usuwamy go więc ze zbioru I.
Wyciągamy kolejny koniec z kolejki i dopóki są >= od danego, to usuwamy. Algorytm jest poprawny, ponieważ  
jeżeli znajdziemy przedział A, kończący się za naszym aktualnie rozważanym, to dzięki posortowaniu po początkach
mamy pewność, że zaczynał się on przed aktualnie rozważanym, a więc jest deaktywowany. 
'''
import math
from heapq import heappop,heappush
h=[]

# do kopca dodajemy wartości przeciwne (-), by móc z kopca min wyciągać wartość max

def intervals(arr):
    arr.sort()
    print(arr)
    
    # oznaczamy, które przedziały bierzemy
    taken=[True]*len(arr)
    for i in range(len(arr)):

        while(len(h)!=0):
            # usuwamy max liczbę przedziałów dezaktywowanych przez aktualny
            Max,idx=heappop(h)
            Max=-1*Max

            if arr[i][1] <= Max :
                taken[idx]=False
            else:
                heappush(h,(-1*Max,idx))
                break
        # do kopca dodajemy koniec przedziału (na minusie) oraz indeks przedziału w tablicy, by łatwo usuwać
        heappush(h,(-1*arr[i][1],i))
    
    for i in range(len(taken)):
        if taken[i] is True:
            print(arr[i])
   
    return taken


