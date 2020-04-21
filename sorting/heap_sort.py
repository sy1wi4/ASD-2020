def heapify(tab, n, i):     #i=indeks, n=rozmiar
    #2*i+1 to lewy syn a prawy to 2*i+2
    largest = i  #na poczatku najwiekszy to korzen
    l = 2 * i + 1     #lewy syn
    r = 2 * i + 2     #prawy syn 
  
    #sprawdzam czy nie wychodze za tablice oraz czy lewy syn jest wiekszy od ojca
    if l < n and tab[i] <tab[l]: 
        largest = l 
    #to samo spr dla prawego syna
    if r < n and tab[largest] < tab[r]: 
        largest = r 
    #teraz largest to nawiekszy element sposrod ojca i jego synow
    if largest != i: #jesli nie korzen nie jest najwiekszy, to musze zamienic largest z i (by largest byl ojcem)
        tab[i],tab[largest] = tab[largest],tab[i] 
        heapify(tab, n, largest) #i to samo robie po zamianie, bo zmienilam i musze naprawic byc moze pod nim
        
def heap_sort(tab): 
    n = len(tab) #rozmiar kopca
    for i in range(n, -1, -1): #zaczynam od ostatniego i az do zerowego lece
        heapify(tab, n, i)
    for i in range(n-1, 0, -1): #wyciagam elementy z kopca
        tab[i], tab[0] = tab[0], tab[i] #max element z indeksem 0
        #wiec jego dajemy na koniec naszej nieposortowanej listy
        #"i" ito rozmiar kopca ktory znow musimy zrobic na kopiec max
        heapify(tab, i, 0)


tab=[43,2,8,7,4,655,3,22]
print(tab)
heap_sort(tab)
print(tab)
