'''Dana jest tablica n liczb A. Proszę podać i zaimplementować
algorytm, który sprawdza, czy da się wybrać podciąg (nie musi byc spojny!!) 
liczb z A, które sumują się do zadanej wartości T'''


# zlozonosc to 2^(n+1)-1 --> worst case

def naiveSum(arr,T,idx):
    #print(T,idx)
    if idx==len(arr) and T!=0 : return False      # doszlismy do konca tablicy i suma!=0 --> nie ma takiej sumy
    if T==0: return True                          # suma sie wyzerowala --> istnieje taki podzbior
    if arr[idx]>T : return naiveSum(arr,T,idx+1)      # suma bedzie mniejsza niz 0, wiec nie biore liczby, wywoluje dla kolejnej
    else: return naiveSum(arr,T-arr[idx],idx+1) or naiveSum(arr,T,idx+1)



# zlozonosc O(n*T)

def dynSum(arr,T):
    n=len(arr)
    dp=[[0]*(n+1) for _ in range(T+1)]       # w wierszach mamy sumy - od 0 do T, w kolumnach dl. przedzialow (od 0)
    
    #chcemy zwrocic wiec dp[T][n]
    
    for i in range(T+1): dp[i][0]=0          # --> nie da sie   | z 0 elementow mozemy jedynie utworzyc sume rowna 0 
    for i in range(n+1): dp[0][i]=1          # --> da sie  | zawsze mozemy utworzyc sume 0 w przedziale, po prostu nie biorac nic 
    
    for suma in range(1,T+1):
        for lenght in range(1,n+1):
            # rozwazam, czy za pomoca elementow o indeksach od 0 do lenght-1 wlacznie uda sie utworzyc sume
            # 1. jesli wartosc ostatniego elementu z danego przedzialu jest wieksza od sumy ktora chcemy uzyskac, to wiem ze jej nie moge wziac
            
            if arr[lenght-1] > suma : dp[suma][lenght]=dp[suma][lenght-1]
            
            # 2. jezeli ten element moze sie zmiescic do sumy, to sprawdzam czy te sume dalo sie utworzyc uzywajac wczesniejszych elementow,
            # tzn ze teraz takze da sie ja utworzyc. Natomiast jezeli wczesniej nie dalo sie, to sprawdzam czy za pomoca wczesniejszyc jestem
            # w stanie utworzyc sume pomniejszona o wartosc tego aktualnego elementu (bo jego moge dobrac i bedzie git), wystarczy nam jedna
            # z tych mozliwosci, zeby sie udalo
            
            else: 
                dp[suma][lenght]=(dp[suma][lenght-1] or dp[suma-arr[lenght-1]][lenght-1])
    
    if dp[suma][n]==1 : return True
    else: return False
    

