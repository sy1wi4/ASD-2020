'''
    Dana jest posortowana rosnąco tablica A wielkości n zawierająca parami różne liczby naturalne. 
    Podaj algorytm, który sprawdzi, czy jest taki indeks i, że A[i] == i.
    Co zmieni się, jeżeli liczby będą po prostu całkowite, niekoniecznie naturalne?
'''

# ALGORYTM :
'''
    Jeżeli liczby są parami różne, to dla j-tego indeksu na lewo są liczby tylko < j, a na prawo tylko > j. 
    Wystarczy  więc sprawdzić, czy A[0] == 0. 
    Jeżeli by tak nie było, wszystkie liczby byłyby “przesunięte” względem swojego własnego indeksu.

    Dla uogólnionego przypadku dowolnych liczb całkowitych poniższe stare rozwiązanie jest prawidłowe:
    Skoro tablica jest posortowana, to dla j-tego indeksu:
    jeżeli A[j] < j, to jeżeli istnieje A[i] == i, to musi być na prawo
    jeżeli A[j] > j, to jeżeli istnieje A[i] == i, to musi być na lewo
    Wystarczy więc wykonać przeszukiwanie binarne z decyzją o tym, gdzie przeszukiwać.
    Złożoność: O(log(n))
'''

def binSearch(arr):
    
    first=0
    last=len(arr)-1
    while(first<=last):
        middle=(first+last)//2
        if(arr[middle]==middle): return middle
        elif(arr[middle]>middle): last=middle-1
        else: first=middle+1
    return False
