'''
Elementem szczytowym jest A[i], tż: A[i-1] <= A[i] >= A[i+1]; elementy brzegowe 
też mogą być szczytowymi, jeżeli A[0] >= A[1] lub A[n-1] >= A[n-2].
Znaleźć algorytm, który zwróci jeden z elementów szczytowych.
'''

# ALGORYTM:
'''
Aby uzyskać złożoność lepszą niż przy zwykłym przejściu tablicy (O(n)), 
możemy użyć czegoś na wzór wyszukiwania połówkowego. Jeżeli prawy sąsiad
danego elementu jest od niego większy, wywyołujemy się rekurencyjnie dla
prawej części tablicy, analogicznie dla lewego. 
O(logn)
'''

def peak(arr,i) :
    if i > 0 and arr[i-1] <= arr[i] and i < len(arr)-1 and arr[i] >= arr[i+1] :
        return arr[i]

    elif i == 0 and arr[i] >= arr[i+1]:
        return arr[i]

    elif i == len(arr)-1 and arr[i] >= len(arr):
        return arr[i]

    elif arr[i-1] >= arr[i] :
        return peak(arr,(i-1)//2)
        
    elif arr[i+1] >= arr[i] :
        return peak(arr,i+(len(arr)-i)//2)

arr=[10,18,9,1,2,5,8]
print(peak(arr,len(arr)//2))
