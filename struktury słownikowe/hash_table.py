'''
Proszę zaimplementować następujące operacje na tablicy haszującej z liniowym rozwiązywaniem konfliktów:
1.  wyszukiwanie
2.  wstawianie
3.  usuwanie (omówić)
'''

class Node:
    def __init__(self,key=None,value=None,state=1):
        self.key=key
        self.value=value
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

def print_table(h):
    print("|",end=" ")
    for i in range(5):
        if h.arr[i] is None: print(None)
        elif h.arr[i].state == 2: print(h.arr[i].key,h.arr[i].value, "r",end=" | ")
        else:
            print(h.arr[i].key,h.arr[i].value,end=" | ")
            
            
def search(table,key):
    index=hash_func(key,table.size)
    cnt=1

    while cnt<=table.size and table.arr[index] is not None:
        if table.arr[index].key==key and table.arr[index].state != 2:
            # kiedy trafimy na odpowiedni klucz i nie został od usunięty wcześniej,
            # tzn że go znaleźliśmy
            return index
        index=(index+1)%table.size
        cnt+=1
    return None

def insert(table,key,value):
    index=hash_func(key,table.size)
    cnt=1   
    # kiedy licznik przekroczy n, przeszliśmy całą tablicę i nie znaleźliśmy miejsca - jest pełna

    while table.arr[index] is not None and table.arr[index].state == 1 and cnt<=table.size :
        index=(index+1)%table.size      
        if(key==0): print(index)
        cnt+=1

    print(index,key,value)
    if cnt==table.size+1: 
        print("table is full",key,value)
    else:
        to_insert=Node(key,value)
        table.arr[index]=to_insert

def remove(table,key):
    index=search(table,key)
    if index is None: print("\nno key",key,"\n")
    else: table.arr[index].state=2

        
