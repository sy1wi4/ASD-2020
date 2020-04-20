'''  Zaproponuj klasę reprezentującą strukturę danych, która w konstruktorze dostaje tablicę liczb
naturalnych długości n o zakresie wartości [0, k]. Ma ona posiadać metodę count_num_in_range(a, b) -
ma ona zwracać informację o tym, ile liczb w zakresie [a, b] było w tablicy, ma działać w czasie O(1).
Można założyć, że zawsze a >= 1, b <= k.  '''
 

'''
Użyjemy counting sorta, ale bez sortowania - zatrzymujemy się na etapie, w którym dostajemy cumulative counts.
Wystarczy dla tej  tablicy zwracać wartość cumul_sum[b] - cumul_sum[a-1],
bo cumul_sum przechowuje ile jest elementów przed nim (lacznie z nim!!!)
'''

from random import randint

class structure:
    def __init__(self,n,k): 
    
        #tworzymy tablice dlugosci n z wartosciami [0,k]        
        self.arr=[]
        
        for _ in range(n):
            self.arr.append(randint(0,k))
        print(self.arr)
        #w konstruktorze zrobimy 'preprocessing' danych - część counting sorta

        self.count=[0]*(k+1) #tablica na wartosci od 0 do k

        for i in range(n):
            self.count[self.arr[i]]+=1
        for i in range(1,k):      #cumulative sum
            self.count[i]+=self.count[i-1]
        
    def countNum(self,a,b):     #zwraca ile liczb w zakresie [a,b]  mamy w tablicy   
        if a!=0 :
            return self.count[b]-self.count[a-1]
        else:
            return self.count[b] 


str=structure(10,5) 
A=str.countNum(1,3)     #zwraca ile liczb z przedzialu [1,3] jest w tablicy
print(A)
