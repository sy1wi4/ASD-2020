''' 
Przewodnik chce przewieźć grupę turystów z miasta A do miasta B. Po drodze jest
jednak wiele innych miast i między różnymi miastami jeżdzą autobusy o różnej pojemności. 
Mamy daną listę trójek postaci (x, y, c), gdzie x i y to miasta między którymi bezpośrednio
jeździ autobus o pojemności c pasażerów. Proszę zaproponować algorytm, który znajduje trasę 
z A do B, po której może przejechać możliwie jak największa grupa turystów bez rozdzielania się.
'''

# ALGORYTM:

# 1. używamy algorytmu podobnego do Dijkstry, z tym, że używamy kolejki priorytetowej typu max 
#    a "relaksacja" krawędzi z u do v polega na tym, że bierzemy minimum z [wagi krawędzi] oraz
#    [większej z wag przypisanych do wierchołków u i v], dzięki czemu weźmiemy największą z możliwych
#    dostępnych pojemności - czyli szukaną liczebność grupy

# 2. szukamy "maksymalnego" drzewa rozpinającego - jego krawędź o najmniejszej wadze to szukana grupa

# 3. BISEKCJA+DFS
#    sortujemy po długościach krawędzie rosnąco, biorę jako przypuszczalnie szukaną wartość środkową i
#    i nie biorąc pod uwagę krawędzi o mniejszej wadze, puszcam DFS i sprawdzam czy zdoła on 
#    odwiedzić miasto B. Jeśli tak, to sprawdzam wartość będącą w połowie stawki powyżej wziętej
#    poprzednio krawędzi, analogicznie jeśli nie - poniżej.
