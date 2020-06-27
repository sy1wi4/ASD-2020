'''
Dane są dwa zbiory liczb, reprezentowane jako tablice rozmiarów m i n, gdzie m jest
znacznie mniejsze od n. Zaproponuj algorytm, który sprawdzi, czy zbiory są rozłączne.

'''

# ALGORYTM:
'''
    sortujemy mniejszą tablicę O(m*log(m)), następnie binsearchem sprawdzamy każdy element z większej tablicy,
    czy jest on w mniejszej O(n*log(m)).

    O( log(m)*(n+m) )
'''

def binSearch(tab,val):
    p=0
    k=len(tab)-1
    while(p<=k):
        s=(p+k)//2
        if(tab[s]==val): return True
        elif(tab[s]>val): k=s-1
        else: p=s+1
    return False

def disjoint(arr1,arr2):
    arr1.sort()     # mlogm
    
    for el in arr2:     # nlogm
        if binSearch(arr1,el): return False,el

    return True
