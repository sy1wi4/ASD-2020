# longest increasing subsequence, tym razem jednak ze zwracaniem wzietych elementow
# utworzymy sobie tablice parentow, gdzie bedziemy trzymac indeks elementu ktory dany element przedluzyl, 
# np P[4]=3 oznacza, ze element o indeksie 4 byl dolozonydo elementu o indeksie 3

from random import randint

def LIS(arr):
    dp=[1]*(len(arr))
    P=[-1]*len(arr)
    # pierwszy element mamy juz dobrze przyporzadkowany
    for i in range(1,len(arr)):
        for j in range(i):    # kandydaci, ktorych chcemy sprobowac rozszerzyc
            if arr[j]<arr[i] :  # jesli ostatni element tego ktory chce rozszerzyc mniejszy to git
                if 1+dp[j]>dp[i]:    # jesli nowa wartosc jest wieksza to zamieniam
                    dp[i]=dp[j]+1
                    P[i]=j  # czyli el. o indeksie i rozszerza el. o indeksie j
    print("dp:\t ",dp)
    print("P:\t ",P)
    x=max(dp)
    for i in range(len(dp)):            #znajdujemy indeks najwiekszej sumy, czyli element o tym idx jest ostatnim z LIS
        if dp[i]==x : idx=i
    res=[]  # tablica z wzietymi wartosciami
    # na poczatku idx to indeks sumy (w dp), czyli tez ostatniego elementu rozwazanego ciagu
    while(idx!=-1):
        res.append(arr[idx])
        idx=P[idx]
    print("taken:\t ",res[::-1])       # odwracam res, zeby byly po kolei
    return x,P


arr=[]
for i in range(9):
    arr.append(randint(1,20))
print("arr:\t ",arr)
a=LIS(arr)
print("len:\t ",a[0])
