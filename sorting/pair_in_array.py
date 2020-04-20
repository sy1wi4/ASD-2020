'''Dana jest tablica zawierająca liczby naturalne. Proszę
zaimplementować funkcję odpowiadającą na pytanie czy
w tablicy jest para sumująca się do jakiejś liczby x.
Funkcja powinna być jak najszybsza.
findPair(arr, x) -> bool.'''

#chcemy miec posortowana tablice, uzyjemy merge sorta

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
          
        #spr czy wszystkie elementy przenieslismy, jesli nie to pozostale sa w dobrej kolejnosci, przenosimy 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1

def findPair(arr,x):
    left=0            #mam indeksy prawego i lewego elementu
    right=len(arr)-1  
#sprawdzam sume prawego i lewego elementu, odpowiednio przesuwam

    while(left<right):
    
        if(arr[right]+arr[left]==x):
            return True
            
        elif(arr[right]+arr[left]<x):
            #musimy zwiekszyc sume
            left=left+1
            
        else:
            #musimy zmniejszyc sume
            right=right-1
            
    return False

arr=[4,2,4,7,8,3,4]
mergeSort(arr)
print(arr)
print(findPair(arr,15))
