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
