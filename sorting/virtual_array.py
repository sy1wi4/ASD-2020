'''
    Dana jest tablica zawierająca liczby całkowite (również ujemne). Należy przeprowadzić preprocessing, 
    tak by móc być w stanie odpowiadać na następujące zapytania w czasie O(log(n)):
    Zapytanie to liczba całkowita x. Podczas odpowiedzi na jedno zapytanie, należy:
    
    “wirtualnie” dodać x do każdego elementu w tablicy
    zwrócić sumę wartości bezwzględnych wszystkich elementów tablicy.

    Uwaga! Dodane “wirtualnie” wartości x akumulują się na kolejne zapytania, tzn. po wykonaniu zapytania 
    dla x=2 “wirtualnie” dodano wszędzie 2, a dla kolejnego zapytania x=3 “wirtualnie” trzeba dodać wszędzie 3, 
    a liczby będą łącznie “wirtualnie” większe o 5 względem tego, co faktycznie jest w tablicy.
'''

# ALGORYTM :
'''
    Sortujemy tablicę. Wyznaczamy tablicę sum prefixowych i suffixowych. Każde zapytanie, to wyszukanie binarnie, 
    gdzie w tablicy zaczynają się elementy, takie, że nawet po dodaniu sumy wszystkich dotychczasowych x z zapytań, 
    będą liczby ujemne. Potem, dla fragmentu liczb dodatnich:
    odpowiednia suma prefixowa + odpowiednia liczba* akumulator wartości x. 
    Dla części ujemnej to samo, tylko przemnażamy przez -1. Złożoność O(nlog(n)).
'''

# zwraca indeks pierwszego elementu, który po dodaniu wszystkich zapytań jest >=0
def binSearch(tab,x):
    p=0
    k=len(tab)-1
    while(p<=k):
        s=(p+k)//2
        if tab[s] + x >= 0 and (s==0 or tab[s-1] + x < 0 ): return s
        elif tab[s] + x < 0 : p=s+1
        else: k=s-1
    return None

class array:
    def __init__(self,arr):
        self.queries=0      # łączna wartość x ze wszystkich zapytań
        self.arr=sorted(arr)
        self.size=len(arr)
        # tablice prefixów i suffixów
        self.prefixes=[None]*(self.size+1)
        self.suffixes=[None]*(self.size+1)

        self.prefixes[0]=0
        for i in range(1,self.size+1):
            self.prefixes[i]=self.prefixes[i-1]+self.arr[i-1]
        
        self.suffixes[-1]=0
        for i in range(self.size-1,-1,-1):
            self.suffixes[i]=self.suffixes[i+1]+self.arr[i]
        

    def query(self,x):
        self.queries+=x
        even=binSearch(self.arr,self.queries)
        
        return (self.suffixes[even] + self.queries*(self.size-even) ) - ( self.prefixes[even] + self.queries*even )
