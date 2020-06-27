'''
    Dana jest nieskończona tablica A, gdzie pierwsze n pozycji zawiera posortowane liczby naturalne, 
    a reszta tablicy ma wartości None. Nie jest dana wartość n. Przedstaw algorytm, który dla danej 
    liczby naturalnej x znajdzie indeks w tablicy, pod którym znajduje się wartość x. Jeżeli nie ma 
    jej w tablicy, to należy zwrócić None.
'''

# ALGORYTM


'''
    Fajnie byłoby użyć wyszukiwania binarnego, ale problemem jest to, że nie znamy prawej 
    granicy liczb. Można ją szybko znaleźć, stosując prostą iterację: skaczemy o i do przodu, 
    sprawdzamy czy jesteśmy na wartości None lub wartości > x - jeżeli tak, to ta pozycja jest naszym prawym końcem 
    i zaczynamy binary search, w przeciwnym wypadku i *= 2 i skaczemy znowu. W ten sposób robimy takie skakanie 
    o kolejne potęgi liczby 2, dzięki czemu w log(n) znajdziemy prawy koniec (być może przeskoczymy n-ty indeks, 
    wchodząc na None, ale nie zaszkodzi to rzędowi złożoności). 
    Następnie wykonujemy binary search, szukając x. 
    
    Dostajemy ostatecznie O(log(n)).
'''

# przekazujemy końcowy indeks tablicy
def binSearch(tab,k,val):
    p=0
    while(p<=k):
        s=(p+k)//2
        if(tab[s]==val): return s
        elif(tab[s] is None or tab[s]>val): k=s-1
        else: p=s+1
    return None

def search(arr,x):
    i=1
    while(arr[i] is not None and arr[i]<=x):
        i*=2

    return binSearch(arr,i,x)
