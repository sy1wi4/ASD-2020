'''Mamy daną tablicę A z n liczbami. Proszę zaproponować algorytm o złożoności O(n), który stwierdza,
czy w tablicy ponad połowa elementów ma jednakową wartość.'''


#bucketsort ale trzymamy takze wielkosc kubelka - jezeli przekroczy n/2, to zwracamy True

def bucketSearch(arr,n):  # n-indeks ostatniego bucketa

    f=False #flaga mowiaca czy znalezlismy wiece niz polowe elementow
    x=(n+1)//2+1    #jesl w ktoryms buckecie bedzie x elementow to zwracam True
    
    Max=max(arr)
    
    buckets=[[] for i in range(n+1)]
    
    for i in range(n+1):      #w kazdym buckecie 1 el. to jego licznosc
        buckets[i].append(0)
        
    for i in range(len(arr)):
        normVal=arr[i]/Max
        bucketIdx=int((n)*normVal)
        buckets[bucketIdx].append(arr[i])
        buckets[bucketIdx][0]+=1    #jezeli dolaczam nowy element, to zwiekszam licznosc odpowiedniego kubelka
        
        if buckets[bucketIdx][0]>=x: f=True
    
    return f
    
