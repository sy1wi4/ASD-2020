'''Dana jest tablica zawierająca n liczb z zakresu [0...n^2-1]. Napisz algorytm, który posortuje taką
tablicę w czasie O(n).'''


'''Należy najpierw posortować countingiem liczby według ich reszty dzielenia przez n a potem też countingiem według ich
wyniku dzielenia (całkowitoliczbowego) przez n.'''

# oba sortowania mają złożoność O(n)


def sort(arr):
    def cSortMod(arr):
    
        n=len(arr)
        # countingSort wg %n
        
        count=[0]*n     # %n przyjmuje wartosci [0,n-1]
        output=[0]*n
        
        for i in range(n):
            count[arr[i]%n]+=1
            
        for i in range(1,n):    #cumulative sum
            count[i]+=count[i-1]
            
        for i in range(n-1,-1,-1):
            output[count[arr[i]%n]-1]=arr[i]
            count[arr[i]%n]-=1
            
        return output

    def cSortDiv(arr):
    
        n=len(arr)
        count=[0]*n      # //n przyjmuje wartosci [0,n-1]
        output=[0]*n
        
        for i in range(n):
            count[arr[i]//n]+=1
            
        for i in range(1,n):
            count[i]+=count[i-1]
            
        for i in range(n-1,-1,-1):
            output[count[arr[i]//n]-1]=arr[i]
            count[arr[i]//n]-=1
            
        return output

    arr1=cSortMod(arr)
    return cSortDiv(arr1)

