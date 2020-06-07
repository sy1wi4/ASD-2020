'''
Dana jest tablica z haszowaniem T[N], w której elementy były wstawiane za pomocą funkcji haszującej 
hash(x) z użyciem liniowego rozwiązywania kolizji. W tej tablicy -1 oznacza wolne miejsce. Proszę 
podać jak najszybszy algorytm sprawdzający, czy dana tablica jest poprawna - czyli, czy każdy element 
może być odnaleziony na podstawie swojego hasha.
'''

# ALGORYTM:
'''
Aby to sprawdzić musimy dowiedzieć się, czy między pozycją liczby a jej hashem jest -1, to 
oznaczałoby, że mogliśmy tam wstawić tę liczbę - tablica jest niepoprawna.
Tworzymy tablicę, która dla każdego indeksu i przechowuje indeks ostatniej -1 przed i w tablicy
haszującej. Po wypełnieniu tej tablicy przechodzimy po tablicy haszującej, wyliczamy hash
danej liczby i patrzymy, czy między nim a naszą liczbą nie ma -1 

'''



def hash_func(key,size):
    # to debug
    return key%size

class hash_table:
    def __init__(self,size):
        self.size=size
        self.arr=[-1]*self.size

def insert(table,key):
    index=hash_func(key,table.size)
    cnt=1   
    # kiedy licznik przekroczy n, przeszliśmy całą tablicę i nie znaleźliśmy miejsca - jest pełna

    while table.arr[index] != -1 and cnt<=table.size :
        index=(index+1)%table.size      
        cnt+=1

    if cnt==table.size+1: 
        print("table is full",key)
    else:
        to_insert=key
        table.arr[index]=to_insert


def is_correct(h):
    array=[None]*h.size

    # najpierw uzupełniamy tablicę array indeksami ostatnich napotkanych -1

    i=0
    # aż do napotkania pierwszej -1 przesuwamy się
    while i<h.size and h.arr[i] != -1:
        i+=1
    for idx in range(i,h.size):
        if idx==i:
            # wypełniamy pierwszą
            array[idx]=idx
        else:
            if h.arr[idx] == -1:
                array[idx]=idx
            else:
                array[idx]=array[idx-1]

    # sprawdzamy, czy tablica jest poprawna
    for i in range(h.size):
        if h.arr[i] != -1:
            current=h.arr[i]
            Hash=hash_func(current,h.size)
            
            if Hash == i: pass  # jest na swoim miejscu - OK
            elif Hash < i:
                # element jest na prawo od miejsca wyznaczonego przez funkcję hashującą
                # sprawdzamy, czy była pomiędzy nimi -1
               if array[i] is not None and array[i]>Hash: 
                   return False
            
            else:
                # element na lewo od hasha
                print(array[i])
                # jeżeli array[i] jest None, tzn, że od początku tablicy nie ma -1
                if array[i] is None:
                    if array[h.size-1] > Hash: 
                        return False
                elif array[i] >= 0 or array[h.size-1] == -1 or array[h.size-1] > Hash:
                    return False
    
    print(array)
    return True

h=hash_table(7)
insert(h,0)
insert(h,3)
insert(h,4)
insert(h,3)
insert(h,3)
insert(h,31)
h.arr[5]=-1

print(is_correct(h))
