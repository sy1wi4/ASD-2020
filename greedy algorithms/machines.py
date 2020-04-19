''' W jednej z chińskich prowincji postanowiono wybudować serię maszyn chroniących ludność przed koronawirusem. 
Prowincję można zobrazować jako tablicę wartości 1 i 0, gdzie arr[i] = 1 oznacza, że w mieście i można zbudować
maszynę, a wartość 0, że nie można. Dana jest również liczba k, która oznacza, że jeśli postawimy maszynę w mieście i,
to miasta o indeksach j takich, że abs(i-j) < k są przez nią chronione. Należy zaproponować algorytm, który stwierdzi
ile minimalnie maszyn potrzeba aby zapewnić ochronę w każdym mieście, lub -1 jeśli jest to niemożliwe. '''

#chronimy k-1 poprzednich oraz k+1 kolejnych

def machines(arr,k):
    last=-1   # zeby pierwsze spr bylo dla miasta o indeksie 0
    counter=0
    notProtected=last+k
    while last<len(arr)-k:  #jesli maszyna jest na ktoryms z ostatnich k miejsc to ochroni reszte miast po niej, wiec nie musimy dalej sprawdzac
        if notProtected>=len(arr):   # jesli ostatnie niechronione jest za tablica, to zaczynam od ostatniego
            notProtected=len(arr)-1
        while arr[notProtected] !=1 and notProtected>=last+1:
            notProtected-=1
        if notProtected ==last:     # tzn ze nie bylo maszyny
            return -1
        else:
            # na miejscu not protected stawiamy maszyne
            last=notProtected
            notProtected+=2*k-1 #kolejne k-1 chronimy, a maksymalnie niechronione moze byc jeszcze o kolejne k dalej(tam najdalej maszyna)
            counter+=1
            
            
    return counter

arr=[1,0,0,0,1,0,0,1,0,0,1,0,1,0,1,0]
k=3
print("min: ",machines(arr,k))
