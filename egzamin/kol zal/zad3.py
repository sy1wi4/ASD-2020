'''
Dana jest tablica A zawierająca n = len(A) liczb naturalnych. Dodatkowo wiadomo, że A w sumie zawiera k różnych liczb (należy założyć, że k 
jest dużo mniejsze niż n). Proszę zaimplementować funkcję longest incomplete(A, k), która zwraca długość najdłuższego spójnego ciągu elementów
z tablicy A, w którym nie występuje wszystkie k liczb. (Można założyć, że podana wartość k jest zawsze prawidłowa.)
'''


# ALGORYTM:
'''
Tworzymy dodatkową tablicę na unikalne elementy - O(nk). Następnie przechodzimy po wejściowej tablicy "gąsienicą",
idąc tak daleko w prawo, aż napotkamy k różnych elementów, co sprawdzamy przechodząc po prostu po k-elementowej
tablicy - O(nk). Zwracamy długość najdłuższego podciągu.
'''

# ZŁOŻONOŚĆ:
'''
O(nk)
'''

def longest_incomplete(A,k):
    n=len(A)

    unique=[None]*k
    counter=[0]*k
   
    # wstawiamy do tablicy k-elementowej unikalne elementy z oryginalnej tablicy
    free=0  # pierwszy wolny indeks w tablicy
    
    for el in A:
        idx=0   # aktualnie rozważany indeks, idziemy od lewej aż do wolnego

        while idx < free :
            if unique[idx] == el:
                break
            else:
                idx += 1
            
        if idx == free :
            unique[free] = el
            free+=1

    

    # idziemy "gąsienicą" po oryginalnej tablicy, zwiększając w tablicy counter odpowiednie liczniki;
    # trzymamy również informacje o najdłuższym dotychczas podciągu i długości aktualnie rozważanego
    #  oraz o ilości już użytych elementów i jeżeli będzie ona równa k, to długość aktualnego podciągu 
    # jest o 1 mniejsza

    
    longest=0       # najdłuższy ogółem
    start=0         # indeks początku danego podciągu
    used=0          # ile unikalnnych elementów użyto
    curr_idx=0      # aktualny indeks
    current_len=0   # długość aktualnie rozważanego podciągu

    # zwraca indeks danego elementu w k-el. tablicy O(k)
    def search(arr,el):
        for i in range(len(arr)):
            if arr[i] == el : 
                return i


    while curr_idx < n:

        if counter[search(unique,A[curr_idx])] == 0 :
            used += 1
        
        counter[search(unique,A[curr_idx])] += 1
        current_len += 1
       
        if used == k :
            longest = max(longest,current_len-1)
            print("licz",counter,"start",start,"used",used,"curr idx",curr_idx,"dlugosc",current_len-1)
            print("kk")
            start += 1
            curr_idx = start
            used = 0
            current_len = 0
            
            # zerujemy
            for i in range(k):
                counter[i] = 0
            
        
        else:
            curr_idx += 1

    return longest
