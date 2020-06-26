'''
Pole wielokąta danego na wejściu jako zbiór współrzędnych kolejnych punktów idąc przeciwnie do ruchu wskazówek zegara.
Iterujemy po tych punktach, jeżeli idziemy na prawo - dodajemy pole trapezu między danym odcinkiem a osią OX, jeżeli
zaś w lewo, odejmujemy to pole. W ten sposób po przejściu wszystkich punktów otrzymamy pole figury wejściowej.
''' 

# pole trapezu między odcinkiem a-b a osią OX
def trapezoid(a,b):

    h=max(b[0],a[0]) - min(b[0],a[0])

    P=(a[1]+b[1])*h/2
    return P 

# tablica krotek - kolejnych punktów tworzących wielokąt (x,y)
def area(arr):
    n=len(arr)

    P=0

    for i in range(n-1):
        x=arr[i][0]

        next_x=arr[i+1][0]

        if next_x > x : 
            P-=trapezoid(arr[i],arr[i+1])
        else:
           P+=trapezoid(arr[i],arr[i+1]) 
    
    x=arr[n-1][0]
    next_x=arr[0][0]
    if next_x > x : 
        P-=trapezoid(arr[n-1],arr[0])
    else:
        P+=trapezoid(arr[n-1],arr[0])
    
    return P
