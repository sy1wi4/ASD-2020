'''
Problem plecakowy - dwuwymiarowa wersja problemu - oprócz ciężaru jest wysokość towarów.
{p1, ..., pn} - przedmioty 
    v(pi) - wartość przedmiotu pi,
    w(pi) - ciężar przedmiotu pi, 
    h(pi) - wysokość przedmiotu pi
Jaka jest największa możliwa sumaryczna wartość przedmiotów, których ciężar
nie przekracza M a wysokość S? Oszacować złożoność i udowodnić poprawność algorytmu.
(Nie trzeba implementować).
'''

# ALGORYTM:
'''
Programowanie dynamicze - tworzymy 3-wymiarowa tablicę, dp[h][w][i] to największa
możliwa wartość, jaką możemy wziąć przy max wysokości h, wadze w oraz przy użyciu 
przedmiotów od 0 do i włącznie. Decydujemy, czy lepiej wziąć i-ty przedmiot, czy nie.
'''
# ZŁOŻONOŚĆ: O( (max_height+1)*(max_weight+1)*(n) )

# przekazuje tablice: W-wagi, P-profity, H-wysokości oraz max wysokość i wagę

def knapsack(W,P,H,max_height,max_weight):  
    n=len(P)

    # 3 wymiarowa tablica H+1 x W+1 x n
    dp=[0]*(max_height+1)
    for i in range(max_height+1):
        dp[i]=[0]*(max_weight+1)
        for j in range(max_weight+1):
            dp[i][j]=[0]*(n)

    for h in range(1,max_height+1):
        for w in range(1,max_weight+1):
            for i in range(n):

                dp[h][w][i]=dp[h][w][i-1]

                # jeśli aktualny (i-ty) przedmiot zmieści się pod względem wagi i wysokości do plecaka)
                if h>=H[i] and w>=W[i] :
                    dp[h][w][i]=max(dp[h][w][i],dp[h-H[i]][w-W[i]][i-1] + P[i])
    
    return dp[max_height][max_weight][n-1]
