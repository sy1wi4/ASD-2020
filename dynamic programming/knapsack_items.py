# Proszę zaimplementować rozwiązanie problemu plecakowego tak, żeby funkcja
# zwracały listę indeksów przedmiotów, które należy wybrać (można korzystać z
# funkcji append do dopisywania elementów na końcu listy).

def knapsackMemo(maxW,W,P):         #funkcja zwracajaca tylko sume
    n=len(W)
    memo=[None]*n
    for i in range(n):
        memo[i]=[None]*(maxW+1)

    return knapsack(maxW,W,P,n-1,memo),memo


def knapsackItems(maxW,W,P):        #funkcja zwracajaca sume i indeksy wzietych elementow
    n=len(W)
    memo=[None]*n
    for i in range(n):
        memo[i]=[None]*(maxW+1)
    a=knapsack(maxW,W,P,n-1,memo)   #zeby to zwrocic
    
    curVal=a               # to co jest suma zwracana 
    curWeight=maxW         # waga maksymalna
    index=[]        # tablica przechowujaca indeksy wzietych elementow
    while(curVal>0 and curWeight>0):
        i=0
        while(memo[i][curWeight] is None or memo[i][curWeight]<curVal):
            i+=1
        index.append(i)
        curVal-=P[i]
        curWeight-=W[i]
    # w ten sposob dostaniemy tablice indeksow uzytych elementow
    #mamy wypelnione memo
    return a,memo,index 

def knapsack(maxW,W,P,idx,memo):
        
        if maxW==0 or idx<0 : return 0
        if W[idx]>maxW :    #jesli sie nie miesci to biore kolejny
            return knapsack(maxW,W,P,idx-1,memo)

        if memo[idx][maxW] is not None:
            return memo[idx][maxW]

        else:
            best=max( P[idx]+knapsack(maxW-W[idx],W,P,idx-1,memo) , knapsack(maxW,W,P,idx-1,memo) )   #bierzemy el idx lub nie
            memo[idx][maxW]=best
            return best
