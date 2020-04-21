def bubbleSort(arr):
    n = len(arr)
 
    for i in range(n):
 
        #ostatnie i elementow na pewno jest na swoim miejscu

        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

