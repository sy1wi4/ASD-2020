'''
. Zbiór przedziałów {[a1, b1], ..., [an, bn]}, każdy przedział należy do [0, 1]. Opisać algorytm który
sprawdzi czy jest możliwy taki wybór przedziałów, aby cały prztedział [0, 1] zawierał się w
wybranych odcinkach. Przedział ma składać się z jak najmniejszej ilości odcinków.
'''
# ALGORYTM:

'''
Dla każdego z przedziałów szukamy najlepszego przedziału kolejnego - takiego, który zaczyna się 
"wewnątrz" danego i kończy jak najpóźniej. Zachłannie wybieramy te najlepsze przedziały zaczynając 
od tego, który zaczyna się w 0 i kończy najdalej. Algorytm ten jest poprawny ponieważ, jeżeli wybierzemy
przedział, który nie kończy się możliwie najdalej, to może okazać się, że potrzebujemy dodatkowego
przedziału, aby "załatać" te pozostałą przestrzeń, której by nie było, jeżeli wzięlibyśmy najdalszy.
'''

# ZŁOŻONOŚĆ: O(n^2) - sprawdzamy dla każdego przedziału wszytskie pozostałe i wybieramy dla niego najlepszy
