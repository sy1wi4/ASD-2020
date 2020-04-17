''' Mamy daną tablicę z nominałami monet stosowanych w pewnym dziwnym kraju, oraz kwotę T. Proszę podać algorytm,
 który oblicza minimalną ilość monet potrzebną do wydania
kwoty T (algorytm zachłanny, wydający najpierw największą monetę, 
nie działa: dla monet 1, 5, 8 wyda kwotę 15 jako 8 + 5 + 1 + 1 zamiast 5 + 5 + 5). '''

# O(T*ilosc nominalow)

# zakladam ze tablica z nominalami jest posortowana rosnaco - jesli nie, to mozemy posortowac
# zauwazmy, ze f(i)= 1 + min(f(i-nom), nom->dostepne nominaly), nasze rozwiazanie to f(n)


def coins(arr,T):
    dp=[0]*(T+1)     # w tablicy przechowuje min ilosc monet dla danej kwoty (rownej indeksowi)
    for i in range(1,T+1):          # dla kazdego elementu szukam najmniejszego rozkladu
        if i-arr[0]>=0:             # jezeli pierwszy nominal "miesci sie" w danej kwocie, jesli nie to kolejnych nawet nie ma po co sprawdzac
            Min=dp[i-arr[0]]        # zakladam ze dla pierwszego nominalu jest najlepsza opcja
            for nom in arr:         # sprawdzam nominaly,dla ktorego jezeli go wezme, to laczna licza monet bedzie najmniejsza
                if i-nom>=0:        # poki nominaly mieszcza sie w kwocie, to spr dla ktorego z nich ilosc mmonet bedzie najmniejsza
                    current=dp[i-nom]
                    if(current<Min): 
                        Min=current
                        
                else : 
                    break
            dp[i]=1+Min
    print("curBest: ",dp)
    return dp[T]

arr=[1,2,4,6,8]
print("number: ",coins(arr,11))
