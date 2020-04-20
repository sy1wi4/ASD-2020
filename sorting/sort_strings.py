'''Mamy daną tablicę stringów, gdzie suma długości wszystkich stringów daje n. Napisz algorytm, który
posortuje tę tablicę w czasie O(n).(Najpierw po dlugosciach, potem leksykograficznie)
Można założyć, że stringi składają się wyłącznie z małych liter alfabetu łacińskiego.'''



#z elementow tablicy robie krotki (dlugosc elementu,wartosc)
def makeTuples(arr):
    for i in range(len(arr)):
        arr[i]=(len(arr[i]),arr[i])
    return arr

#sortowanie stringow:

#ord() – funkcja ord() zwraca liczbę przypisaną do znaku w ASCII
#sortuje wzgledem i-tej pozycji

def countingSort(arr,i):
    letters=ord('z')-ord('a')+1 #ilosc liter od a do z wlacznie
    count=[0]*letters
    output=[0]*len(arr)

    for string in arr:   #kazdy string po kolei 
        count[ord(string[i])-ord('a')]+=1        # zerowy el. tablicy count to 'a' itd, wiec i-ta litera stringa ma indeks ord()=ord('a')

    for j in range(1,len(count)):    # tworze cumulative sum 
        count[j]+=count[j-1]
    
    for p in range(len(arr)-1,-1,-1):     # p to indeksy tablicy wejsciowej arr (od konca)
        count[ord(arr[p][i])-ord('a')]-=1
        output[count[ord(arr[p][i])-ord('a')]]=arr[p]
        
    for i in range(len(arr)):
        arr[i]=output[i]

def radixSort(bucket):  #sortuje stringi jednakowej dlugosci bedace w bucketach
    for i in range(len(bucket[0])-1,-1,-1):
        countingSort(bucket,i)


#najpierw bucket sort po dlugosciach stringow

def bucketSort(arr):
    Max=0   #max dlugosc stringa
    
    for i in range(len(arr)):
        if arr[i][0]>Max: Max=arr[i][0]
    #robimy Max+1 bucketow, w kazdym stringi jednakowej dlugosci
    
    buckets=[[] for i in range(Max+1)]
    for i in range(len(arr)):
        buckets[arr[i][0]].append(arr[i][1])
        
    ctr=0
    
    for bucket in buckets:
        print(ctr," ",bucket)
        ctr+=1
        if len(bucket)!=0:
            radixSort(bucket)

    output=[]
    
    for bucket in buckets:
        output.extend(bucket)
        
    return output
        
