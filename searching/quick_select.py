# k-th statistics - znajdowanie k-tego najmniejszego elementu w tablicy nieposortowanej
# podobne do quickSorta, ale nie wywolujemmy sie dla obu czesci po partition, tylko dla tej, 
# w ktorej jets k-ty element

def partition(arr,p,k) :
    pivot=arr[k]
    idx=p  # tu wwstawiam <= elementy od pivota i przesuwam go w prawo

    for i in range(p,k):
        if arr[i]<=pivot :
            arr[idx],arr[i]=arr[i],arr[idx]
            idx+=1

    # teraz i rozdziela elementy mniejsze i wieksze od pivota 
    # w to miejsce go wstawiam
    arr[idx],arr[k]=arr[k],arr[idx]

    return idx

# wykorzystujemy to, ze po partition pivot jest na swoim miejscu

def quickSelect(arr,l,r,k):  # l-lewy, r-prawy, k-szukany
    idx=partition(arr,l,r)
    if idx-l +1 == k :      # jesli idx jest na k-tej pozycji
        return arr[idx]

    if idx-l+1>k :   # wywolujemy sie dla lewej strony bo k tam jest
        return quickSelect(arr,l,idx-1,k)
    
    else:
        return quickSelect(arr,idx+1,r,k-idx+l-1)
