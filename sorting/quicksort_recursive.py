from random import randint

#napierw dzielimy tablice, nastepnie sortujemy

def partition(tab,p,k):
    pivot=tab[k]    #sortujemy wzgledem ostatniego
    i=p             #i to indeks gdzie bede wstawiac <= elementy(przesuwa sie)
    
    for j in range(p,k):
        if(tab[j]<=pivot):
            tab[j],tab[i]=tab[i],tab[j]
            i=i+1
            
    #gdy przejdziemy cala tab, to zamieniami pivot i-tym elementem,
    #ktory rozdziela elementy mniejsze i wieksze od niego
    
    tab[i],tab[k]=tab[k],tab[i]
    return i    #zwracam indeks pivota

def quickSort(tab,p,k):
    if (p<k):  
        piv=partition(tab,p,k)   #element na dobrym miejscu
        #sortuje lewa i prawa czesc
        quickSort(tab,p,piv-1)
        quickSort(tab,piv+1,k)
