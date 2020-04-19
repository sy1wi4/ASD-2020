Podaj algorytm, który obliczy, ile minimalnie monet trzeba użyć do wydania reszty oraz ile sztuk każdej monety będzie trzeba użyć.
Można założyć, że każdej monety mamy nieskończenie wiele sztuk. '''



def coins(arr,x):
    if x<0: return None
    suma=x
    cnt=0
    res=[0]*len(arr)
    nom=len(arr)-1      # indeks aktualnie uzywanego nominalu
    while(suma>0 and nom>=0):
        while suma/arr[nom]>=1 :
            cnt+=1
            res[nom]+=1
            suma-=arr[nom]
        nom-=1
    print(res)
    return cnt


arr=[1,5,10,25,100]
print(coins(arr,213))
