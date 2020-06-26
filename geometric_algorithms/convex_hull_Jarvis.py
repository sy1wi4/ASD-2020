# OTOCZKA WYPUKŁA - algorytm Jarvisa

'''
Na początek wybieramy punkt, który na pewno należy do otoczki - O (najbardziej na dole, jeśli jest ich więcej,
to ten najbardziej na lewo). Następnie szukamy kolejnego punktu, który znajduje się maksymalnie na prawo,
czyli wybieramy jeden - P, nastepnie porównujemy z pozostałymi (P_n) sprawdzając czy leżą na prawo od odcinka utworzonego
poprzez ostatni punkt otoczki oraz aktualnego kandydata (licząc iloczyn wektorowy wektorów OP_n x OP).
Złożoność algorytmu to O(n*h), gdzie h jest rozmiarem otoczki. 
'''

# położenie p1 względem p2
def location(p1,p2):
    det=p1[0]*p2[1]-p2[0]*p1[1]
    if det > 0 : 
        #na prawo
        return 1

    elif det < 0 : 
        # na lewo
        return -1

    else : 
        # współliniowe
        return 0

def Jarvis_Hull(arr):
    n=len(arr)
    hull=[]
    first=arr[0]

    # szukamy punktu o najmniejszej współrzędnej y (ew. również x)
    for i in range(1,n):
        if arr[i][1] < first[1]:
            first=arr[i]
        
        elif arr[i][1] == first[1]:
            if arr[i][0] < first[0]:
                first=arr[i]

    hull.append(first)   

    # szukamy kolejnych punktów otoczki, wybierając te najbardziej na prawo, gdy dojdziemy do 
    # punktu początkowego kończymy algorytm

    while(True):
        if hull[-1] != arr[0]: current=arr[0]
        else: current=arr[1]
        
        for i in range(1,n):
            hull_x=hull[-1][0]
            hull_y=hull[-1][1]

            if current != hull[-1] and location((arr[i][0]-hull_x,arr[i][1]-hull_y),(current[0]-hull_x,current[1]-hull_y)) == 1 :
                # jeżeli iloczyn wektorowy jest dodatni, czyli któryś z punktów jest bardziej na prawo, to aktualizujemy
                current=arr[i]
            
        if current == hull[0] :
            break

        hull.append(current)
        
    return hull
