'''
    Dana jest tablica  arr o długości m*n, która zawiera parami różne wartości.
    "Pocięto" ją na n kawałków takich samych długości, a następnie losowo poprzestawiano te kawałki.
    Następnie elementy w każdym kawałku także losowo poprzestawiano. Napisz funkcję sortUnsorted(arr, n).
'''

# ALGORYTM:
'''
sortujemy poszczególne kawałki m - elementowe (merge lub quick sortem), a nastepnie względem pierwszych elementów 
tych kawałków sortujemy je

'''

# ZŁOŻONOŚĆ:
'''
posortowanie n kawałków o długości m:  O(n*mlog(m))
posortowanie po pierwszych elementach n kawałków: O(nlog(n))
swapowanie części: O(n*m) 

'''
