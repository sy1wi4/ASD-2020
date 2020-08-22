'''
Algocja leży na wielkiej pustyni i składa się z miast oraz oaz połączonych drogami. Każde miasto jest otoczone murem i ma 
tylko dwie bramy — północną i południową. Z  każdej  bramy  prowadzi dokładnie  jedna  droga  do  jednej  oazy  (ale  do  
danej  oazy  może dochodzić dowolnie wiele dróg; oazy mogą też być połączone drogami między sobą). Prawo Algocji wymaga, 
że jeśli ktoś wjechał do miasta jedną bramą, to musi go opuścić drugą. Szach Algocji postanowił wysłać gońca, który w 
każdym mieście kraju odczyta zakaz formułowaniazadań “o szachownicy” (obraza majestatu). Szach chce, żeby goniec odwiedził 
każde miasto dokładnie raz (ale nie ma ograniczeń na to ile razy odwiedzi każdą z oaz). Goniec wyjeżdżaze stolicji Algocji, 
miasta x, i po odwiedzeniu wszystkich miast ma do niej wrócić. Proszę przedstawić  (bez  implementacji)  algorytm,  
który  stwierdza  czy  odpowiednia  trasa  gońca istnieje.
'''

# ALGORYTM:

'''
Ponieważ (1) z każdego miasta mamy 2 drogi, (2) musimy wejść jedną i wyjść drugą oraz (3) każde miasto chcemy odwiedzić raz, to 
wiemy, że każdą z krawędzi prowadzących z miast możemy użyć dokładnie raz. W tym momecie nasuwa się szukanie cyklu Eulera,
który to przechodzi przez każdą krawędź w grafie dokładnie 1 raz i wraca do wierzchołka startowego. Problem jest tylko z oazami 
- po których możemy się poruszać dowolnie. Należy rozwiązać go tak, że wszystkie oazy, między którymi istnieje bezpośrednia droga 
(krawędź) "łączymy" w jedną super-oazę i traktujemy jak zwykły wierzchołek. Teraz w tak zmodyfikowanym grafie szukamy cyklu Eulera,
sprawdzając, czy stopień każdego z wierzchołków jest parzysty (WK jest także spójność tegoż grafu).
'''
