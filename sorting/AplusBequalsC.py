'''
    Dane są trzy zbiory: A, B i C. Napisz algorytm, który powie, czy istnieje taka trójka a, b, c 
    z odpowiednio A, B, i C, że a + b = c.  Nie wolno korzystać ze słowników!
'''

# ALGORYTM :
'''
    Sortujemy A i B, i dla każdego elementu C, przeprowadzamy szukanie idąc dwoma wskaźnikami: 
    jednym z początku A, drugim z końca B. w zależności od tego, czy suma elementów wskazywanych przez 
    wskaźniki w A i B jest większa lub mniejsza niż element z C, to przesuwamy odpowiedni wskaźnik. 
    Jak natrafimy na równą sumę, to kończymy.

    Inne podejście polega na posortowaniu C i dla każdej pary z A i B szukamy sumy binarnie.

    Złożoności (dla wielkości tablic odpowiednio a, b i c) :

    -pierwsze podejście: O(alog(a) + blog(b) + c(a+b))
    -drugie podejście: O(clog(c) + a*b*log(c)) = O(log(c) * (a*b + c))
'''

# podejście 1

def equal_1(A,B,C):
    A=sorted(A)
    B=sorted(B)



    for num in C:
        a=0
        b=len(B)-1
        while(a<len(A) and b>=0):
            if A[a]+B[b]<num :
                a+=1
            elif A[a]+B[b]>num :
                b-=1
            else:
                print(A[a],"+",B[b],"=",num)
                return True
    return False

# podejście 2

def binSearch(tab,val):
    p=0
    k=len(tab)-1
    while(p<=k):
        s=(p+k)//2
        if(tab[s]==val): return True
        elif(tab[s]>val): k=s-1
        else: p=s+1
    return False


def equal_2(A,B,C):
    C=sorted(C)

    for a in A:
        for b in B:
            if binSearch(C,a+b):
                print(a,"+",b)
                return True
    return False
