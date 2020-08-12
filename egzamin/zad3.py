'''
Pewien eksperyment fizyczny daje w wyniku liczby rzeczywiste postaci a^x, gdzie a to pewna stała większa od 1,
zaś x to liczby rzeczywiste  rozłożone równomiernie na przedziale [0,1]. Napisz funkcję,
która przyjmuje tablicę liczb z wynikami eksperymentu oraz stałą a i zwraca tablicę z wynikami eksperymentu 
posortowanymi rosnąco. Funkcja powinna działać możliwie jak najszybciej. 
'''

# ALGORYTM:
'''
Ponieważ x są rozłożone równomiernie na przedziale [0,1], to możemy użyć bucket sorta, normalizując
dane używając logarytmu o podstawie a.
'''

def ins_sort(tab):

    for i in range(1, len(tab)):
        val = tab[i]  
        j = i - 1 

        while(j >= 0 and val < tab[j]):
            tab[j+1] = tab[j] 
            j = j - 1 

        tab[j+1] = val
    return tab


def fast_sort(tab, a):
    n=len(tab)
    
    buckets = [[] for _ in range(n)] 
    
    for i in tab:
        normNum = i/Max                     # normalizacja: logarytmujemy liczby, dzieki czemu wszystkie beda z przedzialu [0,1]
        bucketIdx = int((n-1) * normNum)    # wybieram bucket
        buckets[bucketIdx].append(i) 


    for i in range(n):
        # kubełki najlepiej sortować insertion sortem
        
        buckets[i] = ins_sort(buckets[i])    
    


    # wpisuję do tablicy posortowane elementy z kolejnych bucketów

    idx=0
    for i in range(n): # i-ty bucket
        if buckets[i] is not None:
            for j in range(len(buckets[i])): # j-ty element
                tab[idx]=buckets[i][j]
                idx += 1

    print("tab",tab)
    return tab
