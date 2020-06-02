'''
Rowerzyści poruszają się po wąskiej ścieżce, mogą jechać tylko jeden za drugim.
Każdy rowerzysta ma swoje id i urządzenie, przez które może przekazać id rowerzysty
jadącego przed nim lub -1 gdy nie ma przed nim nikogo. Napisz funkcję, która otrzymuje
informacje przekazane przez rowerzystów i oblicza rozmiar najmniejszej grupy.
'''

# ALGORYTM:
'''
Problemem jest to, że mając id kolarza przed, możemy się "poruszać" tylko w jedną stronę, więc
nie jesteśmy w stanie określić kto jest ostatni w danej grupie w sposób optymalny.
Możemy rozwiązać to stosując tablicę z hashowaniem i dodając każdemu kolarzowi oprócz id jego 
samego oraz kolarza przed, także id kolarza jadącego za nim. Wstawiając do tablicy hashującej 
(2 razy większej niż wejściowa, by zmniejszyć ryzyko kolizji) ustawiamy każdemu kolarzowi
id następnego na -1 (czyli na razie jakby go nie było). Gdy wszystkich już wstawimy, 
to przechodzimy jeszcze raz po wejściowej tablicy i hashując po id poprzedzającego go znajdujemy,
wpisujemy mu jako id jadącego za nim id aktualnie rozpatrywanego w wejściowej tablicy.
Dzięki temu uzupełnimy każdemu pole id następnego, tylko pierwszy i ostatni z danej grupy 
będą mieli odpowiednio jako id poprzedząjącego i następnego ustawione na -1. Teraz łatwo przejściem
tablicy haszującej możemy obliczyć wielkość grup i wyznaczyć najmniejszą.
'''

class cyclist:
    def __init__(self,ID,prev):
        self.ID=ID
        self.prev=prev  # id jadącego przed (-1 gdy nie widzi nikogo)
        self.next=-1    # id jadącego za (na początku nie wiemy nic)

############################# hash table #######################################################
class Node:
    def __init__(self,cyclist=None,state=1):
        self.cyclist=cyclist
        self.state=state  # defaultowo status pola jest zajęty - gdy wstawiamy
        # state: 1-zajęte, 2-keep looking (bo gdy szukamy elementu, to
        # nie kończymy na tym elemencie, natomiast jeżeli wstawiamy, to tam można wstawić)

def hash_func(key,size):
    return key%size

class hash_table:
    def __init__(self,size):
        self.size=size
        self.arr=[None]*self.size

def insert(table,cyclist):
    index=hash_func(cyclist.ID,table.size)
    cnt=1   
    while table.arr[index] is not None and table.arr[index].state == 1 and cnt<=table.size :
        index=(index+1)%table.size      
        cnt+=1    
    to_insert=Node(cyclist)
    table.arr[index]=to_insert

# flaga change mówi czy zmieniamy pola wyszukiwanych rowerzystów, czy nie
# (w jednym przejściu chcemy zmieniać, w kolejnym nie)
def search(table,cyclist,change=False):   

    key=cyclist.prev

    index=hash_func(key,table.size)
    cnt=1
    while cnt<=table.size and table.arr[index] is not None:
        if table.arr[index].cyclist.ID==key and table.arr[index].state != 2:
            if change: table.arr[index].cyclist.next=cyclist.ID
            return index
        index=(index+1)%table.size
        cnt+=1

def print_table(h):
    print("\n|",end=" ")
    for i in range(h.size):
        if h.arr[i] is None: print(None,end=" | ")
        else:
            print((h.arr[i].cyclist).next,h.arr[i].cyclist.ID,h.arr[i].cyclist.prev,end=" | ")
    print("\n")

################################################################################################

def smallest_group(cyclists):
    size=len(cyclists)
    table=hash_table(2*size)  # 2x większa, by zmniejszyć ryzyko kolizji

    # wstawiamy kolarzy po id do tablicy hashującej
    for i in range(size):
        current=cyclists[i]
        insert(table,current)


    # wyszukujemy po id poprzedzającego danego kolarza
    for i in range(size):
        current=cyclists[i]
        if current.prev != -1 :
            # jeśli dany kolarz widzi kogoś przed sobą, to wpisujemy poprzedzającemu
            # id aktualnego jako jego następnik
            search(table,current,True)
            
    # szukamy w tablicy haszującej kolarza, który jest w danej grupie ostatni

    min_size=float("inf")

    for i in range(2*size):

        if table.arr[i] is not None:
            cur_size=0
            cur_cyclist=table.arr[i].cyclist
            if cur_cyclist.next == -1:
                cur_size+=1
                print(cur_cyclist.ID)
                # kiedy znaleźliśmy pierwszego z danej grupy - kończymy ją analizować
                while(cur_cyclist.prev != -1):
                    idx=search(table,cur_cyclist)
                    cur_cyclist=table.arr[idx].cyclist
                    cur_size+=1
                    print(cur_cyclist.ID)
                print("size",cur_size,"\n")

                if cur_size < min_size: min_size=cur_size

    print_table(table)

    return min_size


# każdy kolarz jako cyclist(ID,prev), next defaultowo na -1, bo na ten moment nic nie wiemy o następnikach
cyclists=[cyclist(5,-1),cyclist(2,5),cyclist(13,3),cyclist(48,-1),cyclist(3,-1),cyclist(10,2)]

print(smallest_group(cyclists))
