'''
Położenie punktu p1 wzgledem p2 w układzie współrzędnych - liczymy iloczyn wektorowy wektorów od 0 do p1 i od 0 do p2,
jeżeli dodatni to zgodnie z ruchem wskazówek zegara, ujemny - przeciwnie, a równy zero oznacza współliniowość

iloczyn wektorowy to pole powierzchni równoległoboku (0,p1,p2,p1+p2) - wyznacznik macierzy:

|x1 x2|
|y1 y2| = x1*y2 - x2*y1

'''

# punkty reprezentowane jako krotki p=(x,y)

def location(p1,p2):
    det=p1[0]*p2[1]-p2[0]*p1[1]
    if det > 0 : print("zgodnie")
    elif det < 0 : print("przeciwnie")
    else : print("współliniowe")

location((1,4),(4,3))
