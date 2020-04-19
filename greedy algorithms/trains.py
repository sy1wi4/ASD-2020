''' Mamy dany pewien rozkład pociągów, dany jako tablica n krotek (arrival_time, departure_time), przy czym są one posortowane 
niemalejąco według arrival_time. Chcemy wiedzieć, czy nasza stacja mająca m peronów jest w stanie bezkonfliktowo obsłużyć
 te pociągi, tzn. w żadnym momencie nie będzie “rywalizacji” pociągów o dostępne perony.
Przedstaw algorytm, który poda odpowiedź True lub False na powyższe pytanie. '''

class train:
    def __init__(self,arrival,departure):
        self.arrival=arrival
        self.departure=departure
    def printTrain(self):
        print("arr: ",self.arrival,"\t  dep: ",self.departure)

def trains(arr,m):
    if len(arr)<=m : return True
    platform=[None]*m    # perony

    for i in range(m):
        platform[i]=arr[i]          # pierwsze m pociagow wpuszczam na peron
       
    
    for j in range(m,len(arr)):            # nadjezdzaja kolejne pociagi
        found=False
        
        for pl in range(m):          # sprawdzam czy na ktorys peron moze wjechac
            if platform[pl].departure <= arr[j].arrival:
                platform[pl]=arr[j]
                found=True      # jesli znalezlismy wolny peron to zaznaczam to
               
                break           # dalej nie musze szukac wolnego peronu
        if not found : return False
    return True
        





a=train(2.00, 2.30)
b=train(2.40, 3.20)
c=train(3.10,3.12)
d=train(3.13,4.40)
e=train(3.20,4.00)
f=train(4.00,5.20)
arr=[a,b,c,d,e,f]       # posortowane po arrival

for train in arr:
    train.printTrain()
