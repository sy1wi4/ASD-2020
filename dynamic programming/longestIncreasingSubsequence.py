# tworzymy tablice, w ktorej dla indeksu i trzymac bedziemy dlugosc LCS od 0 do i wlacznie
# zauwazmy ze f(i)=1 + max(dlugosci wszystkich podciagow, ktore mozemy rozszerzyc i-tym elementem, czyli takich, ze
# wartosc elementu itego jest wieksza od ostatniego wyrazu podciagu rozszerzanego)
# tak wiec teraz z pomocniczej tablicy wystarczy wziac najwiekszy element - to szukana dl. LCS

# złożoność: O(n^2), da się O(nlog(n))

from random import randint

def LIS(arr):
    dp=[1]*(len(arr))
    # pierwszy element mamy juz dobrze przyporzadkowany
    for i in range(1,len(arr)):
        for j in range(i):    # kandydaci, ktorych chcemy sprobowac rozszerzyc
            if arr[j]<arr[i] :  # jesli ostatni element tego ktory chce rozszerzyc mniejszy to ok
                if 1+dp[j]>dp[i]:    # jesli nowa wartosc jest wieksza to zamieniam
                    dp[i]=dp[j]+1
    print("sums: ",dp)
    return max(dp)


arr=[]
for i in range(6):
    arr.append(randint(1,20))
print("arr: ",arr)
print(LIS(arr))
