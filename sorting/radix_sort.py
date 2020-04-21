#sortujemy kolejno "kolumnami" od  najmniej znaczacych cyfr, czyli zaczynajac od ostatniej pozycji az do pierszej
#kazda kolumne sortujemy stabilnym counting sortem

from random import randint

def countingSort(arr,pos):  
    #modyfikacja - sortujemy wzgledem danej cyfry (pos ma wartosci 1, 10 ,100, etc.(cyfra jednosci, dziesiatek...))
    n=len(arr)
    count=10*[0]    #cyfry od 0 do 9
    output=n*[0]
    for i in range(n):
        idx=arr[i]//pos      # "obcinamy" cyfry z konca za ta ktora nas interesuje - idx to cyfry przed wybrana i ona sama
        count[idx%10]+=1    # idx%10 - dostane ostatnia cyfre z pozostalych, czyli ta, ktora mnie interesuje - pos

    for i in range(1,10):
        count[i]+=count[i-1]

    for i in range(n-1,-1,-1):
        idx=arr[i]//pos
        output[count[idx%10]-1]=arr[i]
        count[idx%10]-=1
     
    for i in range(n):
        arr[i]=output[i]


def radixSort(arr):
    Max=max(arr)
    pos=1
    while(Max):
        countingSort(arr,pos)
        Max=Max//pos    
        pos*=10
