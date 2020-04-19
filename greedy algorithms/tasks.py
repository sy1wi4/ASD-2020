def tasks(A):
    # posortujemy tablice wg czasow zakonczenia, biorac kolejne zajecia, ktore sa kompatybilne - mamy pewnosc, ze rozwiazanie bedzie najlepszym
    
    n=len(A)
    A=sorted(A,key=lambda tuple: tuple[1])      # korzystam z funkcji wbudowanej do posortowania tablicy po drugim elemencie krotki
    act=A[0]      # aktualna aktywnosc (ostatnio wybrana)
    res=1
    
    for i in range(1,n):        # szukam najwczesniej konczacych sie zajec, ktore moge wziac
        if A[i][0]>=act[1]:     # jesli zaczynaja sie pozniej niz koncza ostatnio wybrane, to dolaczam
            res+=1
            act=A[i]
    return res


