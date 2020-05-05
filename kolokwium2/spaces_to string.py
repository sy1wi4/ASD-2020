'''
Dana jest zawsze działająca w czasie O(1) funkcja dict(word), która mówi, czy słowo word jest poprawnym słowem 
danego języka. Dostajemy na wejściu stringa bez spacji. Podaj algorytm, który stwierdzi, czy da się tak powstawiać 
spacje do wejściowego stringa, że ciąg słów który otrzymamy tworzą słowa z danego języka. Np. “alamakotainiemapsa” 
możemy zapisać jako “ala ma kota i nie ma psa”. Podaj również, jak wykorzystać algorytm, aby uzyskać przykładowe 
poprawne rodzielenie stringa spacjami, jeśli oczywiście ono istnieje. Algorytm ma być szybki, ale najważniejsze, 
żeby był poprawny!!! 
'''

# ALGORYTM (dynamiczny)

'''
Tworzymy n-elementową tablicę f (wypełnioną wartością False), pod indeksem f[i] jest True lub False, 
w zależności, czy da się pociąć stringa leżącego od indeksu 0 do i włącznie na słowa będące w słowniku. 
Od początku tablicy sprawdzamy, idąc z indeksem i (w pętli), czy istnieje taki indeks j,
że string od j+1 do i włącznie jest w słowniku oraz czy stringa od 0 do j da się pociąć, a to już na tym
etapie wiemy, więc wystarczy sprawdzić wartość f[j]. Czyli:

for i in range(n):
    for j in range(i-1,-1,-1):  # ostatni punkt podziału w 0, stringa ze wszystkich liter sprawdzimy osobno 
                                # bo j wyszłoby za tablicę
        word = [string z liter od j+1 do i]

        if dict(word):
            f(i)=f(i) or f(j)

    # ze wszystkich liter 
    word = [string ze wszystkich liter od 0 do i]
    f(i)=f(i) or dict(word)

'''

# O(n^2)
