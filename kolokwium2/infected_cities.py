'''
Królestwo Syjonu składa się z miast połączonych dwukierunkowymi drogami. Między dowolną parą miast istnieje jedna 
i tylko jedna ścieżka. Część miast została zainfekowana przez maszyny. Do eskalacji ataku dojdzie, jeśli znajdą 
się przynajmniej dwa miasta, zainfekowane przez maszyny, między którymi będzie istniała ścieżka. Dlatego Mofreusz 
postanowił zniszczyć część dróg między miastami, tak aby żadne zainfekowane miasta nie były połączone. Niemniej 
jednak każda droga ma przypisany czas potrzebny  na  zniszczenie. Pomóż Morefuszowi tak dobrać niszczone drogi, 
aby nie instniała ścieżka między dowolnymi zainfekowanymi miastami i czas potrzebny na niszczenie był minimalny. 
Niszczymy jedną drogę na raz.Zadanie ma dwa rozwiązania: dynamiczne i zachłanne, na zajęciach skupimy się na 
zachłannym
'''

# mamy graf spójny, nieskierowany, czyli z warunków zadania wynika, że jest to drzewo

# ALGORYTM:

'''
Ponieważ chcemy usunąć krawędzie o min sumarycznej wadze, to możemy pójść od drugiej strony. Sortujemy
krawędzi nierosnąco i próbujemy daną krawędź dodać do tego zbioru wierzchołków. Jeżeli stworzy ona ścieżkę
między 2 wierzchołkami zainfekowanymi, to nie dodajemy jej. Chcemy dodać krawędzi o jak największych wagach,
ponieważ te, których nie dodamy to te, których szukamy, by  je usunąć, a one mają być jak najmniejsze.
Sprawdzamy to stosując find/union ->  znajdujemy reprezentantów zbiorów do których należą oba wierzchołki,
przechowujemy też dla reprezentanta informację, czy w jego zbiorze jakiś wierzchołek jest zainfekowany.
Jeśli w obu są, to union zwraca False, w przeciwnym razie możemy dodać tę krawędź, czyli połączyć te zbiory 
(musimy także reprezentantowi połączonego zbioru dać info, że ma w zbiorze zainfekowanego, jeśli jeden z 
wierzchołków był).
Te krawędzi, dla których zwróciliśmy False są szukanymi do usunięcia (o najmniejszej sumie czasu niszczenia)
'''

# O(nlog*n)=O(nlogn)   logarytm iterowany
