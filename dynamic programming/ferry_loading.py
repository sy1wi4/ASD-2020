'''
Dana jest tablica A[n] z długościami samochodów, które stoją w kolejce, żeby wjechać na prom. 
Prom ma dwa pasy (lewy i prawy), oba długości D. Proszę napisać program, który wyznacza, 
które samochody powinny pojechać na który pas, żeby na promie zmieściło się jak najwięcej aut.
Auta muszą wjeżdżac w takiej kolejności, w jakiej są podane w tablicy A.
'''

# ALGORYTM 
'''
Rozważać będziemy następujące konfiguracje: k jest liczbą samochodów, które są w danym momencie na promie,
l jest długością lewego pasa, która jest w danej chwili zajęta (znamy więc także zajętą część prawego pasa
- jest to (suma długości samochodów od 0 do k) - l. Zauważmy, że dla konkretnych s i k, możemy dowiedzieć
się, co dzieje się dla k+1 samochodów. Jeżeli możemy wpuścić na prom k samochodów, zajmując przy tym l jednostek
lewego pasa, to:

->  możemy wpuścić k+1 samochód na lewy pas, zajmując (l+długość tego samochodu) jednostek lewego pasa, wtw 
    gdy l+długość nie przekracza D - długości promu

->  możemy wpuścić k+1 samochód na prawy pas, zajmując wciąż l jednostek lewego pasa, ale tylko jeżeli 
    na prawym pasie zajęte jest nie więcej niż D (obliczamy to sumując długości wszystkich k+1 samochodów
    i odejmując długość zajętego lewego pasa (l))

Tworzymy więc  macierz o wymiarach (l+1)x(s+1) i uzupełniamy ją wartościami True bądź False w zależności, czy
dana konfiguracja jest możliwa do utworzenia nie przekraczając długości promu D.
Aby odtworzyć kolejność wjeżdżania na prom tworzymy także macierz rodziców - przechowującą informację,
z której kolumny powyższego wiersza "przyszliśmy" (ile samochodów było na lewym pasie przed wjazdem k+1)

By w O(1) móc uzyskiwać na bieżąco sumę długości k+1 pierwszych samochodów utworzymy tablicę sum prefiksowych.

'''


def ferry_loading(A,D):
    n = len(A)  # liczba samochodów ogółem

    # pomocnicza tablica sum prefiksowych
    pref=[0]*(n+1)
    for i in range(1,n+1) :
        pref[i] = pref[i-1] + A[i-1]


    dp = [[False]*(D+1) for _ in range(n+1)]
    parents = [[None]*(D+1) for _ in range(n+1)]
    
    # pozostałe komórki pierwszego wiersza oprócz dp[0][0] zostawiamy jako False, 
    # ponieważ wpuszczając 0 samochodów, nie możemy zająć więcej niż 0 jednostek lewego pasa
    dp[0][0] = True    

    Max = (0,0)     # krotka przechowująca komórkę w tablicy, dla której liczba samochodów jest największa,
                    # na bieżąco aktualizuję

    # uzupełniamy wierszami macierz według założeń j.w.
    for k in range(n) :
        for s in range(D+1) :
        
            if dp[k][s] is True :
            
                # wpuszczamy k+1 samochód na lewy pas
                if s + A[k] <= D :
                    dp[k+1][s+A[k]] = True
                    parents[k+1][s+A[k]] = s
                    Max = (k+1,s+A[k])
                
                # wpuszczamy k+1 samochód na prawy pas
                if pref[k+1] - s <= D :
                    dp[k+1][s] = True
                    parents[k+1][s] = s
                    Max = (k+1,s)


    # na podstawie macierzy rodziców odtwarzamy, który samochód wpuszczono na lewy,
    # a który na prawy pas, zaczynając od komórki o współrzędnych trzymanych w Max
    # jeżeli rodzic jest w tej samej kolumnie, tzn że aktualny samochód wjechał na prawy 
    # pas, jeżeli w innej - na lewy

    left = [None]*n
    
    row = Max[0]
    col = Max[1]

    while row > 0:
    
        if parents[row][col] == col :

            left[row-1] = False
        else:
            
            left[row-1] = True

        col = parents[row][col]
        row -= 1
   
    
    for i in range(n):

        if left[i] is True:
            print(i,"left")
            
        elif left[i] is False:
            print(i,"right")
            
        else:
            print(i,"no")
            
    return left
        
   
A=[2,3,1,4,2,3]
ferry_loading(A,6)
