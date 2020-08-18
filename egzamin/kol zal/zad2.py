'''
Zauważmy, że dokładając nowy węzeł na początek listy, jego odsyłacze
do pozostałych elementów zachowują się następująco: wystarczy zaczynając od pierwszego elementu
oryginalnej listy i indeksu i=1 brać jego i-ty odsyłacz; idziemy do tego elementu i inkrementujemy
i, bierzemy i-ty odsyłacz, itd. aż lista się skończy (gdy i przekroczy długość tablicy z odsyłaczami).

O(logn)

'''


def fast_list_prepend(L,a):

    start=FastListNode(a)

    if L is None:
      return start

    else:
      start.next.append(L)
      current=L

      i=0
      while i < len(current.next) :
        start.next.append(current.next[i])
        current=current.next[i]
        i += 1
      
    return start



class FastListNode:
  def __init__(self, a):
    self.a = a     # przechowywana liczba calkowita
    self.next = [] # lista odnosnikow do innych elementow; poczatkowo pusta

  def __str__(self): # zwraca zawartosc wezla w postaci napisu
    res = 'a: ' + str(self.a) + '\t' + 'next keys: '
    res += str([n.a for n in self.next])
    return res
