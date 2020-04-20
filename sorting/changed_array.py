'''Masz daną tablicę zawierającą n (n >= 11) liczb naturalnych w zakresie [0, k]. Zamieniono 10 liczb z tej
tablicy na losowe liczby spoza tego zakresu (np. dużo większe lub ujemne). Napisz algorytm, który
posortuje tablicę w czasie O(n).'''


''' Dzielimy tablicę na dwie - te "psujące" 10 elementów i te posortowane (pamiętamy o tym, żeby nie zmienić kolejności!). Sortujemy tę 
10-elementową tablicę (czymkolwiek, bo to czas stały) i je scalamy w czasie O(n). '''


def sort(arr,k):        #przekazuje zakres [0,k]
    #10 elementow jest spoza zakresu, reszta w [0,k] , dziele wiec na dwie tablice
    normal=[]
    out_of_range=[]
    for i in range(len(arr)):
        if arr[i]>=0 and arr[i]<=k :
            normal.append(arr[i])
        else:
            out_of_range.append(arr[i])
    print(normal)
    # te 10 el sortuje obojetnie jak:
    out_of_range=sorted(out_of_range)
    print(out_of_range)
    
    def merge(normal,out_of_range):       #laczenie posortowanych tablicy w 0(n), ale wymaga dodatkowej pamieci
        output=[0]*(len(normal)+len(out_of_range))
        idx=0       # tam wstawiamy
        idx_n=0     # w normal
        idx_o=0     # w out_of_range
        while(idx_n<len(normal) and idx_o<len(out_of_range)):
            if normal[idx_n] <= out_of_range[idx_o] :
                output[idx]=normal[idx_n]
                idx_n+=1
                idx+=1
            else:
                output[idx]=out_of_range[idx_o]
                idx_o+=1
                idx+=1
        #dopelniamy pozostale
        while idx_n<len(normal) :
            output[idx]=normal[idx_n]
            idx+=1
            idx_n+=1
        while idx_o<len(out_of_range):
            output[idx]=out_of_range[idx_o]
            idx+=1
            idx_o+=1
        return output

    a=merge(normal,out_of_range)
    return a


arr=[2,12,2,88,40,6,34,6,6,7,45,8,9]
a=sort(arr,9) # [0,9], zmienione 5 wartosci 
print(a)
