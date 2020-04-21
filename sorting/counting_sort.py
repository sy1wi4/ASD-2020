from random import randint

def countingSort(arr):
    n = len(arr)   
    k = max(arr)
    output = [0] * n      #tablica wyjsciowa tej samej wielkosci co wejsciowa
    count = [0] * (k+1)   #potrzebujemy tablice do zliczenia o wielkosci k (tyle kluczy)

    for i in range(n):     #dla kazdej z wartosci w tablicy zwiekszam element o odpowiednim indeksie o 1
        count[arr[i]] += 1

    for i in range(1,k+1):                  # cumulative sum- teraz wartosc elementu o danym indeksie to ilosc elementow  
        count[i] += count[i - 1]        # mniejszych badz rownych, co pozwoli zachowac stabilnosc algorytmu

    for i in range(n-1, -1, -1):             # umieszczamy kazdy element z tablicy wejsciowej (od konca) w wyjsciowej
        output[count[arr[i]] - 1] = arr[i]   # -1 poniewaz indeksujemy od 0
        count[arr[i]] -= 1

    return output

arr=[]
for i in range(7):
    arr.append(randint(0,30))
print(arr)

print(countingSort(arr))
