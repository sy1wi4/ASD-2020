# struktura zbiorów rozłacznych

class Node:
    def __init__(self,id):
        self.id=id
        self.parent=self    # na poczatku mamy zbiory jednoelementowe, wiec jako rodzic el. wskazuja samych siebie  
        self.rank=0         # wysokosc drzewa

# zwraca rerezentanta zbioru zawierajacego x
def find_set(x) :
    if x != x.parent :
        # rekurencyjnie "pniemy" sie w gore drzewa
        x.parent=find_set(x.parent)
        
    return x.parent # na samej gorze korzystamy z tego ze rodzic x to x


# łączy 2 zbiory w 1 (ten o mniejszej randze dołączamy do tego o większej)
def union(x,y):
    x=find_set(x)
    y=find_set(y)

    if x.rank > y.rank :
        y.parent=x
        
    elif y.rank > x.rank:
        x.parent=y

    else :
        x.parent=y
        y.rank+=1    # po złączeniu drzew o tych samych rozmiarach zwiększamy rozmiar o 1
