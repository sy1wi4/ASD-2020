'''
Dana jest macierz o rozmiarze MxN, zawierająca komórki bezpieczne (o wartości 0 lub 1) 
oraz niebezpieczne (-1). Należy znaleźć ścieżkę o największej liczbie "1", zaczynając 
z komórki matrix[0][0]; możemy poruszać się tylko po komórkach bezpiecznych oraz 
w wierszach parzystych możemy iść tylko w dół lub w prawo, natomiast w nieparzystych 
- w dół lub w lewo.
'''


# ALGORYTM:
'''
Tworzymy macierz pomocniczą dp o wymiarach takich jak wejściowa. W dp[i][j] znajduje się
wartość najlepszej ścieżki kończącej się w komórce matrix[i][j]. Wypełniamy tę macierz
kolejno wierszami. Jeżeli matrix[i][j] ma wartość -1, to wiemy na pewno, że dp[i][j] == 0.
Jeżeli jesteśmy w wierszu parzystym i matrix[i][j] != -1, to bierzemy wartość 
max(dp[i][j-1], dp[i-1][j]) + matrix[i][j], bo mogliśmy przyjść z góry lub z lewej,
analogicznie dla wierszy nieparzystych. Uważamy również na to, by nie wyjść poza  macierz.
'''


# funkcja sprawdzająca czy dana komórka nie wychodzi poza macierz
def ok(M,row,col):
    return row >= 0 and col >= 0 and row < len(M) and col < len(M[0])


def best_path(M):
    dp = [[0]*len(M[0]) for _ in range(len(M))]
    
    best = 0

    for row in range(len(M)) :

        if row % 2 == 0 :
            # wiersz parzysty - z góry lub z lewej
            # wypełniamy od lewej

            for col in range(len(M[0])) :
                if M[row][col] == -1 :
                    dp[row][col] = 0
                
                # osobny przypadek dla pola startowego
                elif row == 0 and col == 0:
                    dp[row][col] = M[row][col]
                    
                else :
                    up = left = 0

                    if ok(dp,row-1,col):
                        up = dp[row-1][col]

                    if ok(dp,row,col-1):
                        left = dp[row][col-1]

                    better = max(up,left)

                    if  better != 0 :
                        dp[row][col] = M[row][col] + better
                        if dp[row][col] > best :
                            best = dp[row][col]
                    
                    else :
                        dp[row][col] = 0
    
        else :
            # wiersz nieparzysty - z góry lub z prawej
            # wypełniamy od prawej

            for col in range(len(M[0])-1,-1,-1) :

                if M[row][col] == -1 :
                    dp[row][col] = 0
                    
                else :
                    up = right = 0

                    if ok(dp,row-1,col):
                        up = dp[row-1][col]

                    if ok(dp,row,col+1):
                        right = dp[row][col+1]

                    better = max(up,right)

                    if  better != 0 :
                        dp[row][col] = M[row][col] + better
                        if dp[row][col] > best :
                            best = dp[row][col]
                    
                    else :
                        dp[row][col] = 0

    return best



M = [
        [1,1,1,1,1],
        [1,0,0,1,1],
        [1,1,-1,1,1],
        [-1,1,1,1,1],
        [1,1,-1,-1,1]
    ]

print(best_path(M))
