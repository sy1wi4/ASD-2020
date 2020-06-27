from random import randint

# n no liczba kubelkow jakie tworzymy, musimy znac ja chociazby przyblizona

def bucketSort(arr, n):
    Max = max(arr)
    buckets = [[] for _ in range(n)] 
    
    for i in arr:
        # normalizacja: dzielimy elementy przez max, dzieki czemu wszystkie beda z przedzialu [0,1]
        normNum = i/Max 
        bucketIdx = int((n-1) * normNum) # wybieram bucket
        buckets[bucketIdx].append(i)     # dodaje liczbe do bucketa
    
    for i in range(n):
        buckets[i] = sorted(buckets[i])     
        #sortuje obojetnie jaka metoda, bo liczba elementow jest stala
    
    output = []
    
    for i in range(n): # i-ty bucket
        for j in range(len(buckets[i])): # j-ty element
            output.append(buckets[i][j])
    return output,buckets


arr=[]
for i in range(10):
    arr.append(randint(0,9))
print(arr)
print()
print(bucketSort(arr,3))
