'''
Dana jest tablica, mamy znaleźć najdłuższy podciąg (niekoniecznie spójny), 
którego elementy są najpierw posortowane rosnąco, a następnie malejąco, np.
[4,2,5,7,6,9,1] -> [2,5,7,9,1]
'''

# ALGORYTM:
''' 
Tworzymy dwie pomocnicze tablice - jedna przechowująca pod indeksem i najdłuższy podciąg 
rosnący kończący się w arr[i] oraz druga, przechowująca najdłuższy podciąg zaczynający się w arr[i].
Następnie sprawdzamy dla każego indeksu wartość sumy inc[i] + dec[i] - 1 oraz wybieramy największą z nich.
Jest to długość szukanego podciągu.
'''

def longest(arr):
    n = len(arr)
    inc = [1]*n  # rosnący
    dec = [1]*n  # malejący


    for i in range(2,n) :
        # sprawdzamy, który podciąg najlepiej rozszerzyć i-tym elementem
        for j in range(i) :
            if arr[i] > arr[j] :
                inc[i] = max(inc[i],1+inc[j])

    
    for i in range(n-2,-1,-1) :
        for j in range(i+1,n) :
            if arr[i] > arr[j] :
                dec[i] = max(dec[i],1+dec[j])

    longest = float("-inf")

    for i in range(n) :
        longest = max(longest, inc[i] + dec[i] - 1)

    return longest
