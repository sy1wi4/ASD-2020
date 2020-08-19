'''
LONGEST-PALINDROMIC-SUBSEQUENCE
Problem znajdowania najdłuższego podciągu (niekoniecznie spójnego) w stringu, będącego palindromem.
'''

# ALGORYTM:
'''
Zaczynamy z indeksami i na początku oraz j na końcu stringa. Jeśli obie litery są takie same, to zwiększamy długość
podciągu o 1 i przesuwamy oba indeksy, jeśli nie, to przesuwamy indeks i lub j, w zależności, który bardziej sie opłaca. 
'''


# naiwny - wykładniczy
def LPS(string,i,j):
    
    if i == j :
        return 1

    elif i > j :
        return 0
    
    elif string[i] == string[j] :
        return 2 + LPS(string,i+1,j-1)
    
    else :
        return max(LPS(string,i+1,j),LPS(string,i,j-1))
    
    
    
# ze spamiętywaniem - O(n^2)
# ulepszenie algorytmu polega na zapamiętaniu w tablicy już raz obliczonej długości 
# najdłuższego palindromu dla danych i oraz j - dzięki temu nie liczymy wielokrotnie tego samego

def LPS_better(string):
    n=len(string)

    memo = [[None]*n for _ in range(n)]


    def lps(string,i,j,memo):

        if i == j :
            return 1

        elif i > j :
            return 0
        
        elif string[i] == string[j] :

            if memo[i][j] is None:
                memo[i][j] = 2 + lps(string,i+1,j-1,memo)
            
    
        else :
            if memo[i][j] is None :
                memo[i][j] = max(lps(string,i+1,j,memo),lps(string,i,j-1,memo))
        
        
        return memo[i][j]
           

    return lps(string,0,len(string)-1,memo)
