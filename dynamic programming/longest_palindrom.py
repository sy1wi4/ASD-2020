'''
LONGEST-PALINDROMIC-SUBSEQUENCE
Problem znajdowania najdłuższego podciągu (niekoniecznie spójnego) w stringu, będącego palindromem.
'''

# ALGORYTM:
'''
Zaczynamy z indeksami i na początku oraz j na końcu stringa. Jeśli obie litery są takie same, to zwiększamy długość
podciągu o 1 i przesuwamy oba indeksy, jeśli nie, to przesuwamy indeks i lub j, w zależności, który bardziej sie opłaca. 
'''


def LPS(string,i,j):
    
    if i == j :
        return 1

    elif i > j :
        return 0
    
    elif string[i] == string[j] :
        return 2 + LPS(string,i+1,j-1)
    
    else :
        return max(LPS(string,i+1,j),LPS(string,i,j-1))

print(LPS("abxaaba",0,6))
