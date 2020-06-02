'''
Jest dana tablica A zawierająca N liczb całkowitych. Szukamy par identycznych elementów, 
które zajmują różne pola w tablicy. Para indeksów (P, Q) jest identyczna, jeżeli 
0 <= P < Q < N oraz A[P] = A[Q]. Napisz algorytm, który zwróci liczbę identycznych 
par indeksów.Przykładowo: A=[3, 5, 6, 3, 3, 5]. Są tutaj 4 pary identycznych indeksów
(0,3); (0,4); (1,5); (3,4). Jako że P < Q, to (2,2) oraz (5, 1) nie są brane pod uwagę.
'''

# ALGORYTM:
'''
Wykorzystamy słownik, wstawiamy do niego kolejne elementy z wartością 1 (ilość elementów 
o tym kluczu w naszej tablicy), jeżeli wstawiamy taki sam element, jaki już jest w tablicy,
to zwiększamy licznik i wartość pod danym kluczem.
'''

class Node:
    def __init__(self,key=None,value=None):
        self.key=key        # wartość w tablicy
        self.value=value    # liczba wystąpień
        

def hash_func(key,size):
    return key%size

class hash_table:
    def __init__(self,size):
        self.size=size
        self.arr=[None]*self.size


def insert(table,key):
    index=hash_func(key,table.size)

    # jeżeli w danym miejscu nie ma żadnej liczby, tzn, że taka jeszcze nie wystąpiła - wstawiamy
    if table.arr[index] is None:
        table.arr[index]=Node(key,1)
        return -1  # flaga, że nie zwiększamy licznika 

    # w przeciwnym wypadku jakaś liczba już tam jest - jeżeli taka sama jak wstawiana to ok, 
    # jeżeli nie, to przesuwamy się, aż trafimy na tą liczbę (albo None, gdy jej nie ma)
    else:
        while table.arr[index] is not None and table.arr[index].key != key :
            index+=1
        if table.arr[index] is None:
            table.arr[index]=Node(key,1)
            return -1
        return index


def print_table(h):
    print("|",end=" ")
    for i in range(h.size):
        if h.arr[i] is None: print(None,end=" | ")
        else:
            print(h.arr[i].key,h.arr[i].value,end=" | ")
    print()

def pairs(arr):
    table=hash_table(len(arr))
    counter=0
    for i in range(len(arr)):
        cur=arr[i]
        
        # znaleziono liczbę - zwiększamy licznik odpowiednio o liczbę jej wystąpień poprzednio 
        idx=insert(table,cur)
        if idx != -1 :
            counter+=table.arr[idx].value
            table.arr[idx].value+=1
    print_table(table)
    return counter


arr=[2,5,4,12,2,2,12,5,9,12,12]
print(pairs(arr))
