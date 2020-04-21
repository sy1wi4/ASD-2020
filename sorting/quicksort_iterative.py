'''  
Proszę zaimplementować algorytm QuickSort (do sortowania tablicy
liczb) w sposób iteracyjny (czyli bez korzystania z rekurencji).
Należy w tym celu wykorzystać własny stos.
'''


def partition(arr,p,k):
    pivot=arr[k]
    i=p;        # indeks gdzie bede wstawiac elementy
    for j in range(p,k):
        if arr[j]<=pivot :
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
    arr[i],arr[k]=arr[k],arr[i]
    return i    #punkt podzialu tablcicy wzgledem pivota (jego indeks)

def qsort(arr,p,k):
    # tworzymy pomocniczy stos
    size=k-p+1
    stack=[0]*size
    top=-1      #gora stosu (gdy -1 tzn ze stos jest pusty)
    #odkladam na stos p i k
    top+=1
    stack[top]=p
    top+=1
    stack[top]=k
    #sciagam ze stosu dopoki nie jest pusty
    while(top>=0):
        k=stack[top]
        top-=1
        p=stack[top]
        top-=1
        pivot=partition(arr,p,k)
        
        #jesli na lewo od pivota sa >=2 el. (by bylo co sortowac)
        if(pivot-1>p):
            top+=1
            stack[top]=p
            top+=1
            stack[top]=pivot-1
            
        #jesli na prawo >=2 el.
        if(pivot+1<k):
            top+=1
            stack[top]=pivot+1
            top+=1
            stack[top]=k
