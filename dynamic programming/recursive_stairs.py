'''
Cel: dana jest tablica A zawierająca liczby naturalne nie mniejsze od 1. początkowo stoimy na pozycji 0;
wartość A[i] informuje nas jaka jest maksymalna długość skoku na następną pozycję. Przykład A=[1,3,2,1,0].
Z pozycji 0 mogę przejść na pozycję 1. z pozycji 1 mogę przejść na 2, 3, 4. Należy policzyć na ile
sposobów mogę przejść z pozycji 0 na pozycję n-1, przestrzegając reguł tablicy.
'''

# ALGORYTM:
'''
W tablicy dp[i] trzymamy liczbę sposobów na dotarcie do pozycji n-1 z pozycji i-tej, wiemy na pewno, 
że dp[n-2] == 1, następnie cofamy się do kolejnych indeksów, zważając na to, jaka jest max długość skoku
i sumujemy liczbę możliwości dla skoków o długości od 1 do max - będzie to po prostu wartość dp[i+długość skoku],
którą już wcześniej obliczyliśmy; jeśli da się doskoczyć z i bezpośrednio do n-1, to dodajemy jedną możliwość.

'''

def stairs(arr):
    n=len(arr)

    # dp[i] to liczba sposobów na dotarcie do pozycji n-1; dp[n-2] == 1 -> ZAWSZE

    dp=[0]*n
    dp[n-2] = 1

    for i in range(n-3,-1,-1):

        Max = arr[i]  # max długość skoku z danej pozycji 

        for j in range(1, Max+1):

            # sumujemy wszystkie możliwości - wartości już wyliczone dla dalszych pozycji,
            # na które możemy z obecnej doskoczyć
            if i+j == n-1 :
                # jeśli możemy skoczyć bezpośrednio na n-1 pozycję, to dodajemy tę jedną możliwość
                dp[i] += 1
                # kończymy, bo dłuższym skokiem wyjdziemy poza tablicę
                break
            else :
                dp[i] += dp[i+j]

    return dp[0]
