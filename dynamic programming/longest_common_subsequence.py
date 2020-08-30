'''
Mamy dane dwie tablice A[n] i B[n]. Należy znaleźć długość ich najdłuższego 
wspólnego podciągu. ( Klasyczny algorytm dynamiczny O(n^2) ).
'''

# ALGORYTM
'''
Tworzymy pomocniczo dwuwymiarową tablicę, w której w dp[i][j] przechowujemy długość
najdłuższego podciągu utworzonego z i pierwszych komórek tablicy A oraz j komórek B.
Rozważając dane długości i oraz j, patrzymy na wartości A[i-1] oraz B[j-1]. Jeżeli są 
równe, to długość podciągu równa jest dp[i-1][j-1] + 1, bo dokładamy do danego podciągu
tę wartość z komórek i-tej oraz j-tej. Natomiast jeżeli te warości są różne, to bierzemy
lepszą z wartości dp[i-1][j] oraz dp[i][j-1].
'''

def LCS(A,B) :
    a = len(A)
    b = len(B)

    # w wierszach rozważamy tablicę B, w kolumnach - A
    dp = [[0]*(a+1) for _ in range(b+1)] 

    for i in range(1,b+1) : 
        for j in range(1,a+1):

            if A[j-1] == B[i-1] :
               dp[i][j] = 1 + dp[i-1][j-1]

            else :
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])

    
    return dp[b][a]
