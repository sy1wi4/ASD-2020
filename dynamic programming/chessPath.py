'''(wędrówka po szachownicy) Dana jest szachownica A o wymiarach n × n. Szachownica
zawiera liczby calkowite. Należy przejść z pola (1, 1) na pole (n, n) korzystając jedynie z ruchów “w dół”
oraz “w prawo”. Wejście na dane pole kosztuje tyle, co znajdująca się tam liczba. Proszę podać algorytm
znajdujący trasę o minimalnym koszcie. '''

from random import randint

def chess(arr,n):

    dp=[[None]*n for _ in range(n)]
    dp[0][0]=0
    for i in range(1,n):
        dp[0][i]=arr[0][i]+dp[0][i-1]       # wypelniam wiersz 0
        dp[i][0]=arr[i][0]+dp[i-1][0]       # wypelniam kolumne 0
        
    for i in range(1,n):
        for j in range(1,n):
            # wpisuje te opcje ktora byla lepsza - z gory czy z prawej
            dp[i][j]=arr[i][j]+min(dp[i][j-1], dp[i-1][j])
            
    
    #bedziemy zwracac ktore komorki bierzemy
    
    row=n-1
    col=n-1
    res=[]
    while row!=0 and col!=0:
        if dp[row][col-1]>dp[row-1][col]:      # czyli przyszlismy z gory
            res.append('↓')
            row-=1
        else:                                  # przyszlismy z lewej
            res.append('->')
            col-=1
    #skonczylismy na indeksie row==0 lub col==0
    if row == 0:
        col-=1   # bo juz pierwszy element z row==0 przylaczylismy juz, wiec zaczynamy od poprzedzajacego
        while(col!=-1):
            res.append('->')
            col-=1
    else:
        row-=1
        while(row!=-1):
            res.append('↓')
            row-=1

    return dp[n-1][n-1],res



n=int(input("wymiar: "))
arr=[[None]*n for _ in range(n)]

for a in arr:
    for i in range(n):
        a[i]=randint(1,9)
    

result=chess(arr,n)
print("min. koszt: ", result[0])
print("sciezka: ",result[1][::-1])
