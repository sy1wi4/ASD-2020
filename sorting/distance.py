'''
    Dane jest n punktów na osi liczbowej jednowymiarowej. Napisz algorytm, który stwierdzi, 
    w którym z nich należy wybudować dom, tak aby suma euklidesowych odległości od tego punktu 
    do wszystkich pozostałych była minimalna. Należy zwrócić również tę sumę. 
    Algorytm powinien być jak najszybszy.
'''

# ALGORYTM

'''
    Najpierw sortujemy punkty. Później będziemy używać dwóch sum odległości (elementów tablicy): 
    wcześniejszych od aktualnego (prefix) oraz późniejszych od aktualnego (suffix). Dzięki nim wystarczy 
    jedno przejście po tablicy, a będziemy cały czas znali odległości do wcześniejszych i późniejszych elementów.
	Dla i-tego elementu wcześniejsze elementy mają położenia 
    A[0], A[1], … , A[i-1], a późniejsze A[i+1], A[i+2], …, A[n - 1].
    Suma odległości do wcześniejszych punktów to  (A[i] - A[0]) + (A[i] - A[1]) + … + (A[i] - A[i - 1]), czyli:
    i * A[i] - (A[0] + A[1] + … + A[i - 1]). Analogicznie dla elementów późniejszych.
	Zauważmy, że jeżeli będziemy trzymali “aktualny” prefix i suffix, czyli “aktualną” sumę elementów 
    wcześniejszych i późniejszych, to wzory sprowadzają się do i * A[i] - prefix oraz suffix - (len(a) - i - 1) * A[i]. 
    Dlatego też podczas iteracji po tablicy na początku prefix = 0, suffix = sum(arr)-A[0], a potem będziemy zwiększać prefix i 
    zmniejszać suffix o A[i], przechodząc dalej. W ten sposób będziemy mieli w pamięci O(1) i kosztem czasowym O(1) aktualną 
    sumę elementów wcześniejszych i późniejszych.
	Policzenie odległości sprowadza się do zastosowania wcześniej wyprowadzonych wzorów: dodajemy odległości do 
    elementów wcześniejszych i do elementów późniejszych, nadążamy za tym dla którego indeksu i jest ona najmniejsza 
    i to zwracamy.
    
    Złożoność: O(nlog(n)) ze względu na sortowanie, sama ta iteracja to O(n)
'''

def distance(arr):
    n=len(arr)
    arr.sort()
    # na początek przed 1 elementem tablicy mamy sumę 0, a za nim sumę wszystkich elementów tablicy bez niego samego
    # aktualizujemy na bieżąco

    prefix=0
    suffix=sum(arr)-arr[0]

    curr_sum=suffix - (n-1) * arr[0]

    for i in range(1,n):
        prefix+=arr[i-1]
        suffix-=arr[i]
        if i*arr[i]-prefix + suffix - (len(arr)-i-1)*arr[i] < curr_sum :
            curr_sum=i*arr[i]-prefix + suffix - (len(arr)-i-1)*arr[i]
            curr_place=i  # aktualnie najlepsze miejsce na wybudowanie domu

    return curr_place,curr_sum
