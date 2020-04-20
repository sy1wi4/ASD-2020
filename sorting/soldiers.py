'''
    W szeregu ustawiło się 2n żołnierzy. Połowa z nich to zwykli szeregowi, a połowa to siły specjalne.
    Mieli się ustawić na 2 grupy: najpierw szeregowi, a potem specjalni, ale sierżant zapomniał im o tym
    powiedzieć. Stoją teraz przypadkowo, z odstępem 1 metra pomiędzy kolejnymi żołnierzami. Szereg to lista struktur typu:
    class Soldier:
        special = False  # is a special soldier?
        next = None
    Zaimplementuj funkcję distance(first), która oblicza najmniejszą liczbę metrów, jaką
    żołnierze muszą sumarycznie przejść, żeby szeregowi stali po lewej od żołnierzy specjalnych 
    (i żeby cały szereg dalej stał w tym samym miejscu).

    Uwaga: nie wymaga się sortowania listy.
'''

# ALGORYTM:
'''
    Nie ruszamy żołnierzy. Idąc kolejno od pierwszego sprawdzamy, czy jest on specjalnym - czyli nie na swoim miejscu.
    Jeżeli tak, to zwiększamy licznik specjalnych (których będą musieli "przejść" szeregowi). Gdy już natrafimy
    na szeregowego to liczba kroków, by wszedł przed pierwszego specjalnego wynosi tyle, ile aktualna liczba specjalnych, 
    jakich już spotkaliśmy. Licznik więc zwiększamy o te liczbę dwukrotnie (bo oboje musieliby się przemieścić).
'''

#ZŁOŻONOŚĆ:   O(n) - musimy tylko sprawdzić każdego żołnierza w szeregu


class Soldier:
    def __init__(self,special):
        self.special=special
        self.next=None

def insertSoldier(first,special):
    if first is None :
        first=Soldier(special)
    else :
        new=Soldier(special)
        new.next=first
        first=new
    return first


def distance(first):
    meters = 0

    # licznik specjalnych
    special_ctr = 0               
    
    soldier = first
    
    while soldier:
        if soldier.special:
            special_ctr += 1
        else:
            meters += 2 * special_ctr
        soldier = soldier.next

    return meters
