'''
Proszę podać algorytm, który mając na wejściu drzewo oblicza skojarzenie o maksymalnej liczności.
'''

# ALGORYTM:
'''
Zauważmy, że drzewo jest grafem dwudzielnym, więc możemy zastosować algorytm do znajdowania 
maksymalnego skojarzenia w grafie dwudzielnym (poprzez dodanie super-źródła i super-ujścia i założenie, 
że każda krawędź ze zbioru A jest skierowana do zbioru B oraz jej przepustowość wynosi 1. Maksymalnym 
skojarzeniem jest maksymalnym przepływ od super-źródła do super-ujścia.)
'''
