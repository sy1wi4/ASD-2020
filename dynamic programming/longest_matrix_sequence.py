'''
Dana jest macierz o rozmiarze NxN. Każda z komórek ma różne wartości - od 1 do N. 
Chcemy znaleźć najdłuższą sekwencję składającą się z sąsiadujących komórek, taką, że
wartość każdej kolejnej sąsiedniej komórki jest o 1 większa od poprzedniej. 
'''


# algorytm naiwny

# f. pomocnicza, sprawdzająca, czy dana komórka nie "wychodzi" poza macierz
def ok(i,j,matrix) :
    return i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix)

def longest_sequence(matrix) :
    
    def longest(matrix,i,j) :
        
        if not ok(i,j,matrix) :
            return 0
        
        # jeśli istnieje sąsiad o wartości większej o 1, to zwiększamy długość aktualnej sekwencji o 1
        else :
            # up
            if i-1 >= 0 and matrix[i-1][j] == matrix[i][j] + 1 :
                return 1 + longest(matrix,i-1,j) 
            
            # down
            if i+1 < len(matrix) and matrix[i+1][j] == matrix[i][j] + 1 : 
                return 1 + longest(matrix,i+1,j) 

            # right
            if j+1 < len(matrix) and matrix[i][j+1] == matrix[i][j] + 1 :
                return 1 + longest(matrix,i,j+1)

            # left
            if j-1 >= 0 and matrix[i][j-1] == matrix[i][j] + 1 :
                return 1 + longest(matrix,i,j-1)

        # nie ma sąsiada o wartości większej o 1
        return 1
    
    # sprawdzamy najdłuższe podciągi zaczynające się w każdej z możliwych komórek, zwracamy najdłuższą z nich
    longest_path = 0

    for i in range(len(matrix)) :
        for j in range(len(matrix)) :
            
            cur_length = longest(matrix,i,j) 
            
            if cur_length > longest_path :
                longest_path = cur_length

   
    return longest_path


# algorytm dynamiczny - ulepszenie algorytmu naiwnego polega na tym, że nie obliczamy wielokrotnie tego samego;
# raz obliczoną długość dla danych i oraz j zapisujemy w tablicy i gdy następnym razem będzie ona potrzebna - po prostu 
# korzystamy z niej

# O(n^2)

def longest_sequence_dynamic(matrix) :
    
    memo = [[1]*len(matrix) for _ in range(len(matrix))]

    def longest_dynamic(matrix,i,j,memo) :
        if not ok(i,j,matrix) :
            return 0
        
        # jeśli istnieje sąsiad o wartości większej o 1, to zwiększamy długość aktualnej sekwencji o 1
        elif memo[i][j] == 1 :
            # up
            if i-1 >= 0 and matrix[i-1][j] == matrix[i][j] + 1 :
                memo[i][j] = 1 + longest_dynamic(matrix,i-1,j,memo) 
            
            # down
            if i+1 < len(matrix) and matrix[i+1][j] == matrix[i][j] + 1 : 
                memo[i][j] = 1 + longest_dynamic(matrix,i+1,j,memo) 

            # right
            if j+1 < len(matrix) and matrix[i][j+1] == matrix[i][j] + 1 :
                memo[i][j] =  1 + longest_dynamic(matrix,i,j+1,memo)

            # left
            if j-1 >= 0 and matrix[i][j-1] == matrix[i][j] + 1 :
                memo[i][j] = 1 + longest_dynamic(matrix,i,j-1,memo)

        # nie ma sąsiada o wartości większej o 1
        return memo[i][j]
    
    # sprawdzamy najdłuższe podciągi zaczynające się w każdej z możliwych komórek, zwracamy najdłuższą z nich
    longest_path = 0

    for i in range(len(matrix)) :
        for j in range(len(matrix)) :
            
            cur_length = longest_dynamic(matrix,i,j,memo) 
            if cur_length > longest_path :
                longest_path = cur_length

   
    return longest_path
