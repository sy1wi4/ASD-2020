from random import randint

def knapsack(items,leftWeight):
    n=len(items)
    W=[]
    P=[]
    for i in range(n):
        W.append(items[i][0])
        P.append(items[i][1])
   
    F=[[0]*(leftWeight+1) for _ in range(n)]
    for i in range(W[0],leftWeight+1):
        F[0][i]=P[0]

    for i in range(1,n):      # kazdy wiersz
        for w in range(1,leftWeight+1):      #kazda kolumna (waga)
            F[i][w]=F[i-1][w]
            if w>=W[i]:     # jesli aktualna max waga plecaka w pomiesci wage W[i] elementu i-tego
                F[i][w]=max(F[i][w], F[i-1][w-W[i]]+P[i])
   
    return F[n-1][leftWeight]




items=[(3,3),(3,1),(2,2),(5,2)]
print(" W  P")
for i in range (4):
    print(items[i])
print("\n")
print(knapsack(items,4),"\n")
