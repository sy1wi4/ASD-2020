'''
Pewna firma przechowuje dużo liczb pierwszych w postaci binarnej jako stringi "10101...". Zaimplementuj 
strukturę danych Set do przechowywania tych danych. 
Powinna wspierać metody:

    •konstruktor Set(A), który tworzy Set z listy stringów A
    •contains(s), która sprawdza, czy dana liczba jest w Secie

Oszacuj złożoność czasową i pamięciową powyższych funkcji.
'''

# ALGORYTM:
'''
Tworzymy następujące drzewo binarne: root nie ma wartości, następnie lewe dziecko ma wartość 0,
a prawe 1, dodatkowo każdy węzeł zawiera flagę, czy kończy jakiegoś stringa. Przechodzimy po kolejnych 
stringach kierując sie w odpowiednie strony (jeżeli 0 to w lewo, 1 - w prawo). Jeżeli chcemy iść 
np. w lewo, ale nie ma tam węzła, to go tworzymy. Gdy przejdziemy po całym napisie odznaczamy flagą, 
że tu się on kończy. Powtarzamy dla każdego napisu.
Sprawdzenie, czy liczba znajduje się w secie opiera się na podobnej zasadzie - idziemy zgodnie z tym
czy mamy 0 czy 1 aż do momentu aż nie będzie się dało dalej pójść (brak węzła). Jeżeli sprawdzimy
cały napis, to patrzymy czy w tym miejscu jest flaga ustawiona na True - jeśli tak, to szukany napis 
jest w secie.
'''

# ZŁOŻONOŚĆ:
'''
Wstawienie: 
    czasowa:     O(n*m), gdzie m to średnia długość napisu, bo wstawiamy n napisów, dla każdego musimy zejść w dół
                 o jego długość
    pamięciowa:  O(2^m), gdzie m to długość najdłuższego wyrazu - m będzie wysokością tworzonego drzewa, a więc 
                 max możemy mieć w nim 2^m węzłów

Sprawdzenie: 
    czasowa:     O(m), gdzie m to długość najdłuższego napisu, bo musimy przejść m węzłów wgłąb
    pamięciowa:  O(1)

'''


class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.left=None
        self.right=None
        self.is_end=False

class Set:
    def __init__(self,strings):
        self.root=Node(None,None)

        for string in strings:
            cur_node=self.root

            for i in range(len(string)):
                num=string[i]

                if int(num) == 0:
                    if cur_node.left is None:
                        cur_node.left=Node(0,0)
                    cur_node=cur_node.left
                    
                elif int(num) == 1:
                    if cur_node.right is None:
                        cur_node.right=Node(1,1)
                    cur_node=cur_node.right

                if i == len(string)-1:
                    # ostatni element stringa - odznaczamy
                    cur_node.is_end=True

    def contains(self,string):
        cur_node=self.root
        for i in range(len(string)):
                num=string[i]

                if int(num) == 0:
                    if cur_node.left is None:
                        return False
                    cur_node=cur_node.left
                    
                elif int(num) == 1:
                    if cur_node.right is None:
                        return False
                    cur_node=cur_node.right 

                if i == len(string)-1:
                    # ostatni element stringa - sprawdzamy czy w 
                    # tym miejscu kończy się string
                    return cur_node.is_end
    


strings=["101000","10110110","0011010","0110","011001","101","0001"]
s=Set(strings)
root=s.root
display_tree(root)

print(s.contains("01101"))
