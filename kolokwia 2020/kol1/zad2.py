'''
Mamy n żołnierzy różnego wzrostu i nieuporządkowaną tablicę, w której podano wzrosty żołnierzy. Żołnierze zostaną ustawieni na placu w szeregu malejąco
względem wzrostu. Proszę zaimplementować funkcję: section(T,p,q)która zwróci tablicę ze wzrostami żołnierzy na pozycjach od p do q włącznie. 
Użyty algorytm powinien  być  możliwie  jak  najszybszy. 
'''

# OPIS ALGORYTMU: wyszukujemy wzrost zolnierza na pozycji p oraz na pozycji q korzystając z algorytmu median of medians --> 2*O(n)
# nastepnie przechodzimy tablice sprawdzajac, ktore ze wzrostow zawieraja sie w przedziale [p,q]

#ZŁOŻONOŚĆ : O(3n)=O(n)

# moglibyśmy też użyć QuickSelecta, otrzymując od razu między indkesami p i q elementy, które nas interesują, natomiast
# jeżeli weźmiemy po uwagę przypadek pesymistyczny to złożoność tego algorytmu to n^2 

# wyszukiwanie i-tego co do kolejnosci  elementu (w szczegolnosci mediany), złożoność algorytmu: O(n)

def partition(tab,p,k):
    pivot=tab[k]  #sortujemy wzgledem ostatniego
    i=p  #i to indeks gdzie bede wstawiac <= elementy(przesuwa sie)
    for j in range(p,k):
        if(tab[j]<=pivot):
            tab[j],tab[i]=tab[i],tab[j]
            i=i+1

    #gdy przejdziemy cala tab, to zamieniami pivot i-tym elementem,
    #ktory rozdziela el mniejsze i wieksze od niego
    tab[i],tab[k]=tab[k],tab[i]
    return i    #zwracam indeks pivota

def quickSort(tab,p,k):
    if (p<k):   #zeby bylo co sortowac

        piv=partition(tab,p,k)   #element na dobrym miejscu
        
        #sortuje lewa i prawa czesc
        quickSort(tab,p,piv-1)
        quickSort(tab,piv+1,k)

def med_of_med(arr,i):

    # lista list 5 elementowych, zawierajaca kolejne elementy wejsciowej tablicy
    lists=[arr[j:j+5] for j in range(0,len(arr),5)]     
    
    # tworze liste zawierajaca mediane kazdej z 5-el. list
    # musimy posortować te listy, ale ze względu na to, że mają 5 elementów zdaje się, że algorytm nie ma tutaj znaczenia 
    #(dla bezpieczeństwa użyjemy quicksorta)

    medians=[None for _ in range(len(lists))]
    idx=0

    for List in lists :
        quickSort(List,0,len(List)-1)
        medians[idx]=List[len(List)//2]
        idx+=1
        
    
    #szukam pivota mediany median w zaleznosci jak dluga jest lista 'medians'
    
    if len(medians) <= 5 :
        quickSort(medians,0,len(medians)-1)
        pivot=medians[len(medians)//2]
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



# korzystamy z powyższego algorytmu, by znaleźć elementy o indeksach p oraz q
# poniewaz med_of_med zwraca elementy przy posortowaniu rosnaco, my bedziemy chcieli znalezc odpowiednio:
# p-ty element przy posortowanej malejąco tablicy, czyli element o indeksie len(T)-1-p, gdy ta tablica bedzie posortowana malejaco
# oraz odpowiednio  q-ty element będzie miał indeks przy posortowaniu rosnąco tej samej tablicy: len(T)-1-q

def section(T,p,q):
    q_th=med_of_med(T,len(T)-1-q)
    p_th=med_of_med(T,len(T)-1-p)
    # mamy p-ty i q-ty element w tablicy, teraz wystarczy juz tylko raz przejsc liniowo nasza tablice
    # i wziac te elementy, ktore zawieraja sie w przedziale[p,q]
    
    res=[None for _ in range(q-p+1)]
    idx=0
    for i in range(len(T)):
        if T[i]>=q_th and T[i]<=p_th :
            res[idx]=T[i]
            idx+=1
    
    return res
