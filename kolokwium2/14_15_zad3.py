'''
Forma to koniunkcja klauzul. Klauzula to alternatywa zmiennych lub ich negacji. Przykład:
(¬a or b) and (¬b or c or d) and (a or d) and (¬a or ¬c or d). Forma składa się z m klauzul
(C1, ..., Cm). Jest n zmiennych (x1, ..., xn). Jak ustawić zmienne, aby co najmniej połowa klauzul
była spełniona? Oszacować złożoność i udowodnić poprawność algorytmu.
(Nie trzeba implementować).
'''

# ALGORYTM:
'''
Wystarczy, że na początek na przykład wartościujemy każdą zmienną jako true.
Następnie przechodzimy po wszystkich klauzulach i sprawdzamy, czy jest tam choć jedna
niezanegowana zmienna. Jeśli tak, to oznacza, że ta klauzula jest spełniona. 
Kiedy już sprawdzimy je wszystkie, to jeżeli spełnionych jest co najmniej połowa, to 
mamy spełniony warunek zadania. Natomiast jeżeli nie, to wszystkie zmienne 
wartościujemy jako false. Ponieważ mamy do czynienia z alternatywą zmiennych, to
gdy wcześniej ponad połowa była niespełniona, to wartościując zmienne przeciwnie 
automatycznie każda ze wcześniej niespełnionych klauzul jest teraz spełniona.
Stąd mamy pewność, że na pewno algorytm jest poprawny.
'''

# ZŁOŻONOŚĆ: o(m), dokładniej O(ilość występujących w klauzulach zmiennych lub ich negacji)
