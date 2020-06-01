'''
Tablica hashująca przechowuje nieujemne elementy. Doskonałością tablicy nazywamy
liczbę elementów x takich, że x w tablicy to hash(x) % size, czyli x jest na "swojej"
pozycji. Napisz funkcję enlarge(table), która powiększa tablicę 2x i wpisujemy elementy
tak, by doskonałość była jak największa. Funkcja powinna być możliwie najszybsza.
'''

# ALGORYTM:
'''
Przechodzimy po naszej tablicy i wyliczamy dla każdego elementu hash w nowej, większej tablicy.
Jeżeli jest on "doskonały", to wpisujemy i odznaczamy ten element w pierwotnej tablicy (np jako None).
Jeżeli nie, to pomijamy element i idziemy dalej. Dzięki temu osiągniemy największą możliwą
doskonałość, ze względu na to, że nie zajmiemy miejsc liczbom, które mogą być na doskonałej
pozycji, ponieważ w pierwszej kolejności przenosimy te, które tam być mogą. Następnie przechodzimy
jeszcze raz po wejściowej tablicy i przepisujemy pozostałe elementy tam gdzie wskazuje nam 
funkcja hashująca - lecz nie zwiększy  to już doskonałości.
'''

class Node:
    def __init__(self,key=None,state=1):
        self.key=key
        self.state=state  # defaultowo status pola jest zajęty - gdy wstawiamy
        # (jeżeli w danej komórce None to pusta) 
        # state: 1-zajęte, 2-keep looking (bo gdy szukamy elementu, to
        # nie kończymy na tym elemencie, natomiast jeżeli wstawiamy, to tam można wstawić)

def hash_func(key,size):
    # to debug
    return key%size

class hash_table:
    def __init__(self,size):
        self.size=size
        self.arr=[None]*self.size

# flaga exc mówi nam, czy po prostu wstawiamy do tablicy(False), czy wstawiamy tylko
# jeżeli osiągniemy doskonałość

def insert(table,key,exc=False):
    index=hash_func(key,table.size)
    cnt=1   
    # kiedy licznik przekroczy n, przeszliśmy całą tablicę i nie znaleźliśmy miejsca - jest pełna
  
    while table.arr[index] is not None and table.arr[index].state == 1 and cnt<=table.size :
        index=(index+1)%table.size     
        cnt+=1
    

    if cnt==table.size+1: 
        print("table is full, cannot insert ",key)
    else:
        if exc:
            if index==hash_func(key,table.size): # jest na swoim indeksie - wstawiamy
                to_insert=Node(key)
                table.arr[index]=to_insert
                return True # wstawiono
            return False    # nie wstawiono

        else:
            to_insert=Node(key)
            table.arr[index]=to_insert
            

def enlarge(table):
    new_size=table.size*2
    new_table=hash_table(new_size)
    
    ctr=0 # licznik doskonałości

    for i in range(table.size):
        curr_key=table.arr[i]
        if curr_key is not None:
            
            if insert(new_table,curr_key.key,True) is True:
                # wstawiono element na swoje miejsce w nowej tablicy - zaznaczamy to w wejściowej
                table.arr[i]=None
                ctr+=1
    
    # pozostałe elementy wpisujemy wg hashu
    for i in range(table.size):
        if table.arr[i] is not None:
            insert(new_table,table.arr[i].key)

    return ctr
