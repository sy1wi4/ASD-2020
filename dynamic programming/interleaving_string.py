'''
Dane są 3 stringi. Należy stwierdzić, czy ostatni (długości m+n) składa się 
z liter pierwszego i drugiego (odpwiednio długości m oraz n).
Kolejność liter w słowach musi zostać zachowana, np:
ABC, CD, ACBCD --> True
'''

# ALGORYTM:
'''
Problemem w zadaniu są litery występujące wielokrotnie - nie wiemy, czy wziąć literę z 1 stringa, czy z 2.
Np. dla danych stringów: ABC, ACD, ACDABC jeżeli weźmiemy "A" z 1 stringa, to zwrócimy False, trzeba wziąć 
"A" z drugiego stringa, wtedy reguły są zachowane.

Tworzymy więc pomocniczą tablicę o wymiarach (m+1) x (n+1), w której dp[i][j] oznacza, czy z 
i pierwszych liter pierwszego stringa oraz j liter drugiego stringa da się utworzyć trzeciego
(i+j pierwszych liter). Wiemy na pewno, że dp[0][0] == True, następnie wypełniamy kolejne wiersze:
jeżeli dp[i-1][j] == True, to sprawdzamy, czy i - ta litera pierwszego stringa zgadza się z i+j - tą
literą trzeciego stringa. Jeśli tak, to dp[i][j] == True, jeśli nie, to analogicznie sprawdzamy dla 
j - tą literę drugiego stringa. Jeśli żadna z nich nie pasuje, to dp[i][j] = False.
Szukane rozwiązanie problemu to wartość w komórce dp[m][n].
'''

def strings(A,B,C):
    m=len(A)
    n=len(B)

    if len(C) != m+n :
        return False

    dp = [[None]*(n+1) for _ in range(m+1)] 
    
    for i in range(m+1) :
        for j in range(n+1) :

            if i == j == 0 :
                dp[i][j] = True

            elif i >= 0 and dp[i-1][j] is True :
                dp[i][j] = (C[i+j-1] == A[i-1])

            elif j >= 0 and dp[i][j-1] is True :
                if dp[i][j] is True :
                    continue
                else:
                    dp[i][j] = (C[i+j-1] == B[j-1])
            
            else :
                dp[i][j] = False


    return dp[m][n]


print(strings("ABC","ACD","ACDABC"))
