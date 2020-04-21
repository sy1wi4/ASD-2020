def sort(tab):
    for i in range(1,len(tab)):
        val=tab[i]  #to bede wstawiac
        j=i-1
        while(j>=0 and val<tab[j]):
            tab[j+1]=tab[j]     #przesuwam elementy tablicy w prawo
            j=j-1
            
        #i jak juz znajdziemy miejsce dla val, to wstawiamy(w miejsce j+1)
        tab[j+1]=val

tab=[4,7,2,9,1]
sort(tab)
print(tab)
