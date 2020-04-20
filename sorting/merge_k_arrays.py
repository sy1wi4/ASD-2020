'''
    Zaproponuj algorytm scalający k posortowanych
    tablic w jedną posortowaną tablicę. Łączna liczba
    elementów we wszystkich tablicach wynosi n.
    Algorytm powinien najlepiej działać w czasie
    O(n*log(k)).
'''

from collections import deque
import heapq
from random import randint

max_value = 100

def generate_data(n, k):
    lists = [[] for i in range(k)]
    while n >= 0:
        list_index = randint(0, k - 1)
        lists[list_index].append(randint(0, max_value))
        n -= 1

    # uzywamy kolejki by moc sciagac w czasie O(1)
    lists = [deque(sorted(lists[i])) for i in range(k)]
    return lists


def print_lists(lists):
    for x in lists:
        print(list(x))



# OPIS ALGORYTMU:

"""
    Bierzemy pierwszy element z każdej listy i tworzymy kopiec min zawierający tuple 
    (val, indeks listy). Dzięki temu moze znaleźć listę z najmniejszym elementem w czasie O(log(k)).
    Następnie wyciągamy z kopca ten element i kolejny element z tej listy dodajemy do kopca
    i naprawiamy go
"""
# ZŁOŻONOŚĆ:

'''
    n razy dodajemy element do kopca i naprawiamy go: O(n*log(k))
'''


def merge_lists(lists, n):

    k = len(lists)
    first_elems = []
    for k in range(0, len(lists)):
        # sprawdzamy czy lista nie jest pusta

        if lists[k]:
            first_elem = lists[k][0]
            first_elems.append((first_elem, k))

    # z listy first_elems tworzymy kopiec
    heapq.heapify(first_elems)

    result = []
    while len(result) < n:
        # bierzemy najmniejszy element z kopca
        elem, index = heapq.heappop(first_elems)

        # element sciagniety z kopca mozemy juz usunac z tablicy wejsciowej
        lists[index].popleft()

        # element za usunietym dodajemy do kopca 

        if lists[index]:
            new_elem = lists[index][0]
            heapq.heappush(first_elems, (new_elem, index))

        # dodajemy uprzednio zdjety z kopca i usuniety z tablicy element to tablicy wynikowej
        result.append(elem)

    return result

