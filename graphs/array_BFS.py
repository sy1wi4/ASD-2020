'''
Dana jest tablica 0 i 1.
Gracz początkowo znajduje się na (zadanej) pozycji (x, y), dla której zachodzi A[x][y] == 1.
Z danej pozycji wolno bezpośrednio przejść jedynie na pozycję, której dokładnie jedna
współrzędna różni się o 1, oraz której wartość w tablicy A wynosi true. Proszę napisać program
obliczający do ilu różnych pozycji może dojść gracz startując z zadanej pozycji (x, y).
'''

# ALGORYTM 
'''
Uruchamiamy algorytm BFS na tablicy
'''

from collections import deque



def BFS(arr,x,y):
    
    q=deque()
    size=len(arr)

    # tworzymy pomocniczą tablicę, czy odwiedzony
    visited=[[False]*size for _ in range(size)]

    q.appendleft((x,y))  
    visited[x][y]=True

    # licznik odwiedzonych pól 
    ctr=0

    while(len(q)!=0):

        a,b=q.pop()

        #przeglądamy wszystkie pola, na które możemy się dostać z (a,b)
        
        pos_x=[a-1,a+1,a,a]
        pos_y=[b,b,b-1,b+1]

        for i in range(4):
            if len(q)==0 : q=deque()

            x=pos_x[i]
            y=pos_y[i]
            
            if x >= 0 and x < size and y >= 0 and y < size :
                
                if arr[x][y] ==1 and visited[x][y] is False :
                    visited[x][y]=True
                    ctr += 1
                    q.appendleft((x,y))
                    


    return ctr
