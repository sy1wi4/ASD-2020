'''W problemie tankowania paliwa nasz pojazd musi przemieścić się z punktu 0 do punktu F, a po drodze ma stacje do 
tankowania paliwa si, przy czym 0 < s1 < s2 < ... < sn < F. Każda stacja jest identyfikowana przez jej odległość od punktu 0, 
tzn. si to odległość pomiędzy i-tą stacją a puntem 0. Pojazd potrafi przejechać odległość d bez potrzeby tankowania.
Podaj algorytm, który obliczy, na ilu minimalnie stacjach musi zatrzymać się pojazd na drodze od punktu 0 do punktu F.
Uwaga: jeżeli zdarzy się, że odległość d jest zbyt mała, żeby dojechać do kolejnej stacji, to należy zwrócić wartość None. '''


def fuel(arr,d,F):  # tablica przechowuje odleglosci od pktu poczatkowego
    
    curLocation=0
    res=0                  #liczba stacji na jakich musimy sie zatrzymac
    lastStation=0          #stacja na ktorej ostatnio tankowalismy, zeby nie spr od poczatku za kazdym razem
    
    while True:
        
        if F-curLocation<=d:  # tzn ze moge ten odcinek przejechac bez zatrzymywania sie na stacji
            return res
        
        else:
            reached=curLocation+d           # tu moge najdalej dojechac na baku
            idx=lastStation                 # ostatnio odwiedzona stacja 
           
            while(idx+1<len(arr) and arr[idx+1]<=reached):
                idx+=1
            
            # jako idx mamy najdalsza stacja z ktorej mozemy skorzystac
            
            if(idx==lastStation):       # jesli nie zwiekszylismy idx ani razu tzn ze nie bylo stacji na drodze
                return None              # nie bylo stacji po drodze
            
            else: 
                lastStation=idx
                res+=1
                curLocation=arr[idx]
                
