'''
Szachownica NxN, ustawiono pewną ilość skoczków. Opisać algorytm który sprawdzi czy jest
możliwa sekwencja ruchów spełniająca:
- każdy ruch kończy się zbiciem skoczka
- sekwencja kończy się gdy zostanie jeden skoczek.
'''

# ALGORYTM:

'''
Mamy daną tablicę, którą będziemy interpretować jako graf - krawędź, jeżeli istnieje możliwość zbicia między
danymi 2 skoczkami. Cały algorytm sprowadza się do sprawdzenia czy taki graf jest spójny - jeśli tak, to jest
możliwa taka sekwencja. Sprawdzamy jednym przejściem DFSa, czy odwiedzi on wszystkie pozycje, na których są skoczki.
'''
