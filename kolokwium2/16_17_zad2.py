'''
Złodziej widzi na wystawie po kolei n przedmiotów o wartościach A[0], A[1], ..., A[n − 1]. Złodziej
chce wybrać przedmioty o jak największej wartości, ale resztki przyzwoitości zabraniają mu
ukraść dwa przedmioty leżące obok siebie. Proszę zaimplementować funkcję goodThief(arr);
która zwraca maksymalną wartość przedmiotów, które złodziej może ukraść zgodnie ze swoim
kodeksem moralnym oraz wypisuje numery przemiotów które powinien wybrać. Proszę uzasadnić
poprawność algorytmu oraz oszacować jego złożoność czasową. Algorytm powinien być możliwie
jak najszybszy (ale przede wszystkim poprawny).
'''

def goodThief(arr):
    n=len(arr)

    stolen=[False]*n
    dp=[0]*n

    # w tablicy dp wartość i-tego elementu to max wartość dla przedmiotów od 0 do i włącznie
    
    dp[0]=arr[0]
    dp[1]=max(arr[0],arr[1])

    for i in range(2,n):
        
        # decyduję, czy lepiej wziąć i-ty przedmiot, czy nie
        dp[i]=max(dp[i-1],dp[i-2]+arr[i])
        
    
    for i in range(n-1,1,-1) :
        if dp[i-2]+arr[i] == dp[i] and (i==n-1 or stolen[i+1] is False) : stolen[i]=True
    
    if stolen[2] : stolen[0]=True
    else : 
        if arr[0]>arr[1] : stolen[0]=True
        else: stolen[1]=True
    
    # wypisywanie wziętych przedmiotów

    print("stolen:",end=" ")
    for i in range(n):
        if stolen[i] : print(arr[i],end=" ")  
    print()  

    return dp[n-1]
