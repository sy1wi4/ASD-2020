'''
    Dana jest formuła logiczna w postaci 2CNF. To znaczy, że formuła jest koniunkcją klauzuli,
    gdzie każda klauzula to alternatywa dwóch literałów, a każdy literał to zmienna lub jej negacja.
    Przykładem formuły w postaci 2CNF nad zmiennymi x,y,z jest: (x ∨ y) ∧ ( ~x ∨ z ) ∧ ( ~z ∨ ~y).
    Proszę podać algorytm, który w czasie wielomianowym stwierdza, czy istnieje wartościowanie spełniające formułę.
'''

# 2-SAT is a special case of Boolean Satisfiability Problem and can be solved in polynomial time.


# ALGORYTM:

'''
    Zauważmy, że każdą alternatywę dwóch literałów można przedstawić jako dwie implikacje, np:
    (x v y) = ( ~x => y ) ∧ (~y => x), ponieważ jeżeli jeden jest fałszywy, to na pewno drugi musi
    byc prawdziwy, by cała klauzula była prawdziwa.

    Możemy więc całą daną formułę przedstawić jako graf implikacji, w którym dla każdej klauzuli 
    mamy dwie krawędzi.

    Wiemy też, że:
        (x => y) = (y => x),

        jeżeli (x => ~x), to wiemy, że x=0
        jeżeli (~x => x), to wiemy, że x=1
        więc jeżeli w grafie istnieją dwie powyższe krawędzi, to nie ma wartościowania spełniającego
        formułę, ponieważ x musiałoby jednocześnie być prawdziwe i fałszywe

        jeżeli (x => y) ∧ (y => z), to wiemy, że (x => z), czyli mając ścieżkę w grafie, jest to
        równoznaczne z tym, że mogłaby istnieć taka bezpośrednia krawędź

        jeżeli w jednej silnie spójnej składowej jest x i ~x, to False, ponieważ z def. SSC (Strongly
        Connected Component) jeżeli 2 wierzchołki są w jednej, to istnieje ściezka w obie strony, co nie
        może mieć miejsca (opisano wyżej).

    -----------------------------------------------------------------------------------------------------------
    Żeby nie dopuścić do sprzeczności  przy wartościowaniu (może być tak że x jest osiągalny z ~x i odwrotnie,
    lecz NIE JEDNOCZEŚNIE), należy posortować topologicznie silnie spójne składowe,
    wtedy jeżeli SCC z x jest przed SCC z ~x, to x=0, analogicznie odwrotnie.
'''

# po prostu SCC i sprawdzamy, czy zmienna i jej zaprzeczenie nie należą do tej samej składowej
