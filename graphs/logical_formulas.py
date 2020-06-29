'''
Dana  jest  formuła  logiczna postaci: C1 ∧ C2 ∧ ··· ∧ Cm, gdzie każda Ci to klauzula będąca alternatywą zmiennych
i/lub ich zaprzeczeń. Wiadomo, że każda zmienna występuje w formule dokładnie dwa razy, raz zanegowana i raz niezanegowana.
Na przykład poniższa formuła stanowi dopuszczalne wejście: (x ∨ y ∨ z) ∧ (~y ∨ w) ∧ (~z ∨ v) ∧ (~x ∨ ~w) ∧ (~v). 
Proszę podać algorytm, który oblicza takie wartości zmiennych, że formuła jest prawdziwa.
'''

# ALGORYTM:
''' 
Tworzymy graf dwudzielny, w którym jednym ze zbiorów są zmienne (tu: v,w,x,y,z), drugim formuły logiczne.
Jeżeli dana zmienna występuje w formule (zaprzeczona lub nie), to łączymy je krawędzią. Każda krawędź ma 
przepustowość równą 1. Teraz wystarczy wyznaczyć maksymalne skojarzenie w tym grafie dwudzielnym. Jeżeli
w skojarzeniu jest dana krawędź (między zmienną a formułą), to znaczy, że ta zmienna ma wartość 1 jeżeli 
nie jest zaprzeczona lub 0 w.p.p. Takie rozumowanie jest poprawne, ponieważ w skojarzeniu może być maksymalnie
jedna krawędź wychodząca od danej zmiennej (czyli nie będzie sytuacji, że ma ona jednocześnie wartość 1 i 0,
co prowadziłoby do sprzeczności). Ponadto ponieważ każda klauzula jest alternatywą zmiennych, to wystarczy,
że wartościowanie jednej jest 1, by formuła była prawdziwa. Dzięki temu, gdy znajdziemy maksymalne skojarzenie,
wystarczy sprawdzić, czy jest ono równe liczebności zbioru B (tj. czy każda formuła może być spełniona).
'''
