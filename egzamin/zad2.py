'''
Asystent znanego profesora otrzymał polecenie wyliczenia sumy pewnego ciągu liczb (liczby mogą być zarówno dodatnie jak i ujemne):
n1+n2+...+nk. Aby zminimalizować błędy zaokrągleń asystent postanowił wykonać powyższe dodawania w takiej kolejności, by największy 
co do wartości bezwzględnej wynik tymczasowy (wynik każdej operacji dodawania; wartość końcowej sumy również traktujemy jak wynik tymczasowy) 
był możliwie jak najmniejszy.  Aby  ułatwić  sobie  zadanie,  asystent  nie  zmienia  kolejności  liczb  w  sumie  a  jedynie wybiera kolejność
dodawań. Napisz funkcję, która przyjmuje tablicę liczb n1, n2, . . . , nk (w kolejności w jakiej występują w sumie; zakładamy, że tablica 
zawiera co najmniej dwie liczby) i zwraca największą wartość bezwzględną  wyniku  tymczasowego  w  optymalnej  kolejności  dodawań.  Na  przykład  
dla  tablicy wejściowej: [1,−5,2] funkcja powinna zwrócić wartość 3, co odpowiada dodaniu −5 i 2 a następnie dodaniu 1 do wyniku.
'''



# funckje zwracające liczbę o odpowiednio mniejszej/większej wartości bezwzględnej

def min_abs_val(a,b):
    if abs(a) < abs(b) : 
        return a
    else:
        return b

def max_abs_val(a,b):
    if abs(a) > abs(b) : 
        return a
    else:
        return b



def opt_sum(tab):
    # aby mieć na bieżąco dostęp do sumy w danym przedziale tworzymy sobie 
    # pomocniczo tablicę sum prefixowych - wtedy suma [i,j] to pref[j+1] - pref[i]

    n=len(tab)
    prefix=[None]*(n+1)
    prefix[0]=0
    
    for i in range(1,n+1):
        prefix[i]=prefix[i-1] + tab[i-1]
    
    memo=[[0]*n for _ in range(n)]
    # w memo[i][j] zapamiętujemy wartość sumy tymczasowej, której wartość bezwzględna
    # na danym przedziale jest minimalna (z maksymalnych)

    # rozważamy coraz dłuższe przedziały
    for length in range(1,n):

        for start in range(n-length):
            end = start + length

            # na początek do memo wpisujemy sumę danego przedziału - wyliczoną za pomocą
            # tablicy sum prefiksowych

            memo[start][end] = prefix[end+1] - prefix[start]

            # dla każdego przedziału sprawdzamy, które 2 podprzedziały najlepiej
            # dodać do siebie (tak, by max suma tymczasowa była jak najmniejsza)
            # k jest "punktem podziału", bierzemy przedziały [start][k] oraz [k+1][end]
            
            best = float("inf")
            
            for k in range(start,end):
                best = min_abs_val(max_abs_val(memo[start][k], memo[k+1][end]), best)

            # do memo wpisujemy wartość z najlepszego podziału lub sumę całego przedziału,
            # jeśli jej wartość bezwzględna jest większa

            memo[start][end]=max_abs_val(best,memo[start][end])

    return abs(memo[0][n-1])
