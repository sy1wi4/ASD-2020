'''
Mamy dany graf G=(V, E) z wagami jako dodatnie liczby naturalne.
Chcemy  znaleźć  scieżkę  z  wierzchołka u do v tak,  by  iloczyn  wag  był  minimalny.
Proszę zaproponować algorytm.
'''

# ALGORYTM

# używamy algorytmu Dijkstry, ale z pewną modyfikacją - logarytmujemy wagi krawędzi,
# dzięki czemu liczby nie będą aż tak szybko rosły oraz możemy wykorzystać własność:
# log(x) + log(y) =log(xy), dzięki czemu chcąc minimalizować iloczyn wag krawędzi,
# możemy tak naprawdę minimalizować sumą logarytmów 
