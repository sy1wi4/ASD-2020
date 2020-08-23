'''
Dana jest macierz binarna o rozmiarze MxN. Mamy znaleźć największą kwadratową pod-macierz
składającą się wyłącznie z "1".
'''

# ALGORYTM

'''
Zauważmy, że zachodzi następująca własność:

rozmiar największej podmacierzy "kończącej" się w komórce M[i][j] jest o 1 większy
niż minimum z rozmiarów podmacierzy kończących się w M[i-1][j], M[i][j-1], M[i-1][j-1].
Jeżeli więc komórka M[i][j] jest "otoczona" przez 3 macierze 2x2 (oczywiście nachodzące na siebie),
to dokładając do nich komórkę M[i][j], jeżeli wartość w niej wynosi 1, otrzymujemy macierz o wymiarach 3x3.
Utwórzmy więc pomocniczą macierz o tym samym rozmiarze, co macierz wejściowa, w której trzymać będziemy 
w dp[i][j] rozmiar największej macierzy kończącej się w komórce M[i][j]. Wystraczy zwrócić największą
wartość z tablicy dp.

O(n^2)

'''

def largest_matrix(M):
    dp=[[0]*len(M[0]) for _ in range(len(M))]

    # wypełniamy pierwszy wiersz od góry i od prawej - jeśli 1, to max rozmiar to 1, jeśli 0 - 0
    for i in range(len(M[0])):
        dp[0][i] = M[0][i]

    for i in range(len(M)):
        dp[i][0] = M[i][0]


    # wypełniamy pozostałe komórki powyższą metodą, dodatkowo przetrzymujemy dotychczas największą podmacierz
    largest = 0

    for col in range(len(M[0])) :
        for row in range(len(M)) :

            if M[row][col] == 0 :
                dp[row][col] = 0
            else:
                dp[row][col] = 1 + min(dp[row-1][col],dp[row][col-1],dp[row-1][col-1])
                if dp[row][col] > largest :
                    largest = dp[row][col]


    return largest
