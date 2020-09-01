''' implementacja kolejki priorytetowej min jako kopiec '''


# w 0 komorce przechowuje rozmiar kopca
def size(k): 
    return k[0]  


# przy heapify zakladam ze drzewa zaczepione w synach sa naprawione, tylko el. i moze byc mniejszy,
# chce sprawic y ta wartosc splynela w dol i wszystko od i w dol bylo posortowane

# naprawia kopiec, O(logn)
def heapify(k,i):         
    left = 2 * i
    right = 2 * i + 1
    Min = i

    if left <= size(k) and k[left] < k[Min] : 
        Min=left

    if right <= size(k) and k[right] < k[Min] :
        Min=right

    # Min to najmniejszy ze sprawdzanej trojki

    if Min != i :  # jezeli kolejnosc jest zla
        k[i],k[Min] = k[Min],k[i]

        heapify(k,Min)  # wywoluje to samo dla zmienianego elementu i sprawdzam jego dzieci


def buildHeap(k):   # O(n)
    for i in range(size(k)//2, 0, -1): # bo zaczynam od rodzica ostatniego dziecka(o indeksie i)
        heapify(k,i)

    # dostaje odpowiedni kopiec min
    return k



# funkcja getmin zwraca najmniejszy element kopca min i naprawia go
def getmin(k):      # O(logn)

    res=k[1]
    k[1]=k[size(k)]
    k[0]=k[0]-1 #rozmiar zmniejszam o 1
    heapify(k,1)
    return res

# wstawia element o wartosci x do kopca i naprawia go
def insert(k,x):    # O(logn)
    # powiekszam kopiec o 1
    k[0]+=1 

    k[size(k)]=x
    i=size(k)

    # musze teraz sprawdzic czy nowy element nie zaburza kopca, jesli tak, to zamieniam z rodzicem
    while i > 1 and k[i] < k[i//2] :    # gdzie i//2 to rodzic i-tego elementu
        k[i], k[i//2] = k[i//2], k[i]
        i = i // 2


# przykładowe użycie
arr = [None]*10
arr[0] = 0
buildHeap(arr)
insert(arr,1)
insert(arr,5)
insert(arr,6)
insert(arr,10)
insert(arr,-2)

print(arr)
print(getmin(arr))
