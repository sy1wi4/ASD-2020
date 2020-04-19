''' problem plecakowy, z tym, ze mozemy brac ulamkowe czesci przedmiotow'''

from random import randint

def knapsack(arr,weight):       # arr to tablica krotek (waga, profit)
    print("waga dopuszczalna :", weight,"\n")
    
    #najpierw sortujemy po wadze na jednostke masy
    tab=[[0]*2 for _ in range(len(arr)) ]        # tworzymy tablice 2-elementowych tablic wg takiego wzoru: [profit/waga,indeks]
    
    for i in range(len(arr)):
        tab[i][1]=i
        tab[i][0]=arr[i][1]/arr[i][0]

    tab=(sorted(tab))[::-1]     #posortuje nam tablice wg pierwszego elementu malejaco
    print("[profit/1kg, indeks]: ",tab,"\n")

    profit=0.0          # calkowity koszt przedmiotow ktore zabierzemy, to zwracamy
    curWeight=weight    # waga jaka pozostala do wypelnienia w plecaku
    
    for item in tab:   
        if curWeight>0:
            idx=item[1]                        # tu mamy indeks kolejno coraz mniej cennych elementow
            
            if arr[idx][0]<=curWeight:         # jezeli waga mojego elementu jest mniejsza niz pojemnosc plecaka w danym momencie (miesci sie)
                # jesli tak to biore cala dostepna ilosc
                
                profit+=arr[idx][1]
                curWeight-=arr[idx][0]
            else:                 # przedmiot w calosci nie miesci sie w plecaku, wiec dobieram tyle, ile brakuje, by go zapelnic
                profit+=curWeight*arr[idx][1]/arr[idx][0]
                curWeight=0
               
    return profit

