def mergeSort(arr): 

    if len(arr) >1: 
        mid = len(arr)//2 #znajduje srodek tablicy
        #dziele tablice na dwie czesci
        
        L = arr[:mid]  #od 0 do srodka(bez)
        R = arr[mid:]  #od srodka(wlacznie) do konca
        
        #powtarzam dla obu czesci
        mergeSort(L)
        mergeSort(R)  
        
  #wywoluja sie merge sorty az bede miec pojedyncze elementy
        i = j = k = 0
        #mam 2 posortowane kawalki, lacze je
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        #sprawdzam czy wszystkie elementy przenieslismy, jesli nie to pozostale sa w dobrej kolejnosci, przenosimy 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
  
