'''
Cyfra jednokrotna to taka, która występuje w danej liczbie dokładnie jeden raz. Cyfra wielokrotna to taka, która w liczbie występuje 
więcej niż jeden raz. Mówimy, że liczba naturalna A jest ładniejsza od liczby naturalnej B jeżeli w liczbie A występuje więcej cyfr 
jednokrotnych niż w B, a jeżeli cyfr jednokrotnych jest tyle samo to ładniejsza jest ta liczba, która posiada mniej cyfr wielokrotnych. 
Na przykład: liczba 123 jest ładniejsza od 455, liczba 1266 jest ładniejsza od 114577, a liczby 2344 i 67333 są jednakowo ładne. Dana jest 
tablica T zawierająca liczby naturalne. Proszę zaimplementować funkcję: pretty_sort(T), która sortuje elementy tablicy T od najładniejszych 
do najmniej ładnych. Użyty algorytm powinien  być  możliwie  jak  najszybszy.  
'''


# ALGORYTM:

'''
tworzymy pomocniczą tablicę krotek o rozmiarze n (il. c. jednokrotnych, il. cyfr wielokrotnych, indeks)
sortujemy tablice krotek najpierw względem drugiego elementu krotki od najmniejszego, następnie od największego 
pierwszego elementu krotki. Zauważmy, że ilość wystąpień cyfr jedno/wielokrotnych jest nie większa
niż 10; dzięki temu możemy użyć liniowego algorytmu sortowania - counting sort - liczba kluczy jest
bardzo ograniczona, jest to algorytm stabliny, dzięki czemu mamy pewność, że przy sortowaniu wg kryterium
ważniejszego (tutaj liczba cyfr jednokrotnych), elementy uprzednio posortowane wg kryterium mniej ważnego,
nie poprzestawiają się
'''



# wartość single mówi nam, czy sortujemy wg cyfr jedno czy wielokrotnych (bierzemy pod uwagę odpowiedni
# element krotki); jeśli single == True, to sortujemy malejąco, w.p.p. rosnąco

def countingSort(arr,single):

    n = len(arr)   

    output = [0] * n      # tablica wyjsciowa tej samej wielkosci co wejsciowa
    count = [0] * 11   # potrzebujemy tablice do zliczenia na klucze od 0 do 9

    if single :
        # sortujemy po 1 elemencie krotki - malejąco

        for i in range(n):    # dla kazdej z wartosci w tablicy zwiekszam element o odpowiednim indeksie o 1
            count[arr[i][0]] += 1
            
        for i in range(9,-1,-1):            # cumulative sum- teraz wartosc elementu o danym indeksie to ilosc elementow  
            count[i] += count[i + 1]        # większych badz rownych, co pozwoli zachowac stabilnosc algorytmu

        for i in range(n-1, -1, -1):             # umieszczamy kazdy element z tablicy wejsciowej (od konca) w wyjsciowej
            output[count[arr[i][0]] - 1] = arr[i]   # -1 poniewaz indeksujemy od 0
            count[arr[i][0]] -= 1

    else :
        # sortujemy po 2 elemencie krotki - rosnąco

        for i in range(n):    
            count[arr[i][1]] += 1
            
        for i in range(1,11):                  
            count[i] += count[i - 1]        

        for i in range(n-1, -1, -1):             
            output[count[arr[i][1]] - 1] = arr[i]  
            count[arr[i][1]] -= 1  
    
    return output


def pretty_sort(T):
    
    # pomocnicza tablica do zliczania wystąpień poszczególnych cyfr w danej liczbie
    digit = [0]*10  
    
    # dla każdej liczby z wejściowej tablicy od nowa zliczamy cyfry
    def zeruj(digit) : 
        for i in range(len(digit)) :
            digit[i] = 0
        return digit
  

    # tablica krotek (il. c. jednokrotnych, il. c. wielokrotnych, indeks), uzupełniamy na bieżąco
    new = [None]*len(T)


    # zliczamy
    for i in range(len(T)) :
        current = T[i]
    
        while current :

            digit[current%10] += 1
            current = current // 10
        
        # zapisujemy w tablicy new odpowiednie wartości

        j = w = 0   # liczba cyfr jedno i wielokrotnych

        for idx in range(10) :
            if digit[idx] == 1 :
                j += 1
            
            elif digit[idx] > 1 :
                w += 1

        new[i] = (j,w,i)
        
        digit = zeruj(digit)

    # teraz pozostało posortować tablicę krotek (new); najpierw rosnąco wg 2 elementu krotki, 
    # następnie malejąco wg 1
  
    new = countingSort(new, False)
    new = countingSort(new, True)
    
    # zwracamy posortowane elementy z wejściowej tablicy T wg ich indeksu w kolejności 
    # posortowanej z tablicy new

    result = [None]*len(T)
    for i in range(len(result)):
        result[i] = T[new[i][2]]

    return result
