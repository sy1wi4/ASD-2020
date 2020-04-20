'''
    Zaimplementuj funkcję average_score(arr, n, lowest, highest).
    Funkcja ta przyjmuje na wejściu tablicę n liczb rzeczywistych (ich
    rozkład nie jest znany, ale wszystkie są parami różne) i zwraca
    średnią wartość podanych liczb po odrzuceniu lowest najmniejszych
    oraz highest największych. Zaimplementowana funkcja powinna być
    możliwie jak najszybsza. Oszacuj jej złożoność czasową (oraz bardzo
    krótko uzasadnić to oszacowanie).
'''

'''
    złożoność: O(n)

    Z użyciem algorytmu median of medians szybko dowiemy się, jakie elementy są brzegowe 
    Musimy 2 razy wywołać tę funkcję i przejść liniowo bo tablicy

'''


from random import randint

# wyszukiwanie i-tego co do kolejnosci elementu (w szczegolnosci mediany)    O(n)

def med_of_med(arr,i):

    # lista list 5 elementowych, zawierajaca kolejne elementy wejsciowej tablicy
    lists=[arr[j:j+5] for j in range(0,len(arr),5)]     
    
    # tworze liste zawierajaca mediane kazdej z 5-el. list
    medians=[sorted(List)[len(List)//2] for List in lists] 

    #szukam pivota mediany median w zaleznosci jak dluga jest lista 'medians'
    
    if len(medians) <= 5 :
        pivot=sorted(medians)[len(medians)//2]
    else:
        # rekurencyjnie szukam mediany listy 'medians'
        pivot=med_of_med(medians,len(medians)//2)     
    

    #podzial na mniejsze i wieksze elementy od pivota
    low=[i for i in arr if i<pivot]
    high=[i for i in arr if i>pivot]

    x=len(low)

    #element x-ty (o indeksie x-1) to pivot, na lewo sa mniejsze, na prawo wieksze, wiec spr po ktore stronie lezy szukany i-ty element
    if i<x :       
        return med_of_med(low,i)            # na lewo mamy x-1 elementow
    elif i>x:
        return med_of_med(high, i-x-1)      # na prawo mamy x-k elementow
    else:  
        return pivot

def average_score(arr, n, lowest, highest) :
    # szukam liczby ktora po posortowaniu tablicy bedzie na pozycji lowest - elementy na lewo od niej odrzucamy, 
    # a takze liczby na pozycji len(arr)-1-highest   (elementy na prawo od tego indeksu odrzucamy)
    
    low=med_of_med(arr,lowest)   
    high=med_of_med(arr,len(arr)-1-highest)

    print(low,high)
    sum=0
    for el in arr:
        if el >= low and el <= high :
            sum+=el
    
    number=len(arr)-lowest-highest  # ilosc liczb, ktore bierzemy pod uwage
    average=sum/number
    return average
