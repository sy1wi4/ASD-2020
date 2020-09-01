'''
Proszę opisać algorytm dla następującego problemu: dana jest tablica A zawierająca 
n przedziałów. Elementy tablicy A opisują przedziały otwarte. Dana
jest także liczba t. Zadanie polega na wypisaniu t lub mniej przedziałów, których suma daje spójny
przedział o maksymalnej długości.
'''

# ALGORYTM:
'''
Sortujemy przedziały po początkach, następnie dzielimy je na grupy przedziałów, których sumy są spójne.
Następnie w każdej z grup rozważamy t przedziałów leżacych obok siebie (jeżeli grupa jest mniej liczna to 
bierzemy wszystkie; gąsienicą od 0 do n-t). Jeżeli zazębiają sę wiecej niż 
2 przedziały to dobieramy tylko ten kończący się najdalej (mamy pewność, że poprzedzające są w sumie
krótsze). Gdy już weźmiemy t (lub mniej) przedziałów sprawdzamy jaką długość ma ich suma i jeżeli
jest taka potrzeba, to aktualizujemy najdłuższą dotychczas znalezioną sumę i przedziały, które ją tworzą, 
by móc je potem wypisać. 
'''

# niedokończona implementacja


# funkcja tworząca grupy przedziałów, które w sumie są spójne
def make_groups(arr):
    groups=[]
    idx=0       # indeks aktualnej grupy
    current=0   # indeks aktualnego przedziału

    while(True):
        groups.append([])
        groups[idx].append(arr[current])

        while(arr[current+1][0] <= arr[current][1]):
            groups[idx].append(arr[current+1])

            current+=1
            
            if current == len(arr)-1:
                break
            
        current+=1       
        idx+=1

        # przypadek, gdy zostanie samotny przedział na końcu
        if current == len(arr)-1:
            groups.append([])
            groups[idx].append(arr[current])

        if current >= len(arr)-1:
            break

    return groups
