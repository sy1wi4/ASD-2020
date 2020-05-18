### WARUNKI ###
# korzeń jest czarny
# każdy liść (None) jest czarny
# jeśli węzeł jest czerwony to obaj jego synowie są czarni
# każda prosta ścieżka z ustalonego węzła do liścia ma tyle samo czarnych węzłów

# n - liczba węzłów
# bh - długość czarnej ścieżki
# h - wysokość drzewa
# n>= 2^bh - 1
# h <= 2log(n-1)

# wstawianie (X):   O(logn)
'''
1. wstawiamy jak do drzewa BST, kolorujemy X na czerwono
2  -> jeżeli to korzeń - zmieniamy na czarno, bo z definicji korzeń musi być czarny
   -> jeśli ojciec wstawianego jest czarny to nic nie zmieniamy - nie zaburzymy drzewa
   -> w przeciwnym razie ojciec jest czerwony 

      2.1  wujek X jest czerwony - ojca i wujka kolorujemy na czarno, dziadka na czerwono, jeżeli dziadek
           to root, to kolorujemy go na czarno i kończymy. W przeciwnym razie powtarzamy naprawianie dla dziadka

      2.2  wujek X (na prawo) jest czarny, a X jest prawym dzieckiem 

                        dziadek X (czarny)
                            /    \
           rodzic X (czerwony)  wujek X (czarny)
                    \
                     \
                  X (czerwony)

        Wykonujemy rotację w lewo względem rodzica (krawędzi rodzic-X), następnie dla rodzica, 
        któy po rotacji jest pod X wykonujemy przypadek 2.3

        Analogicznie dla wujka czarnego na lewo a X jest lewym dzieckiem, wykonujemy rotację w lewo
        względem rodzica, a następnie dla rodzica przypadek 2.3
    
      2.3  wujek X (na prawo) jest czarny, X jest lewym dzieckiem

                        dziadek X (czarny)                               rodzic X (czerwony)
                            /    \                                      /            \
           rodzic X (czerwony)  wujek X (czarny)                   X (czerwony)      dziadek X (czarny)
                    /                               ---->                               \               
                   /                                                                   wujek X (czarny)
              X (czerwony)
        
        Wykonujemy rotację w prawo względem dziadka X, a następnie zmieniamy na przeciwne kolory rodzica X i dziadka X
        Teraz rodzic ma taki sam kolor jaki uprzednio dziadek, więc struktura drzewa RB została przywrócona.

        Analogicznie postępujemy, jeżeli wujek X (na lewo) czarny, a X jest prawym dzieckiem.
    
'''
