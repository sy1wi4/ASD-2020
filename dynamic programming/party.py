''' 
ZADANIE: znalezc najwieksza laczna sume 'funu' osob bioracych udzial w imprezie - nie chemy zeby bezposredni 
podwladny i przelozony byli jednoczesnie obecni
''' 
#O(n)

'''sprobujmy jeszcze wypisywac imiona uczestnikow''' 
#O(n)

# pracownik
class Person:
    def __init__(self,name,fun):
        self.fun=fun
        self.name=name
        self.emp=[]      # tablica emp zawiera wszystkich bezposrednich podwladnych danego pracownika
        self.f=-1
        self.g=-1
        self.going=None

        # f i g daja nam info o tym jaki jest max fun dla poddrzewa (z aktualnym pracownikiem jako korzen) - dzieki temu nie zliczam wielokrotnie
        # f - najlepsza impreza w poddrzewie zacczepionym w employee
        # g - najlepsza impreza jezeli nie idzie na nia employee

def f(person):          # najlepsza impreza - decyzja czy lepiej, kiedy person idzie czy nie
    if person.f>=0 : return person.f    # mamy juz te informacje wiec nie musimy jej obliczac
    # person idzie na impreze - szukam max funu dla poddrzewa (na pewno jego podwladni bezposredni nie ida), czyli ta 
    # wartsoc to bedzie wartosc funu person + suma najlepszych imprez, na ktore nie ida jego podwladni (watrosc funkcji g)
    going=person.fun
    for emp in person.emp:
        going+=g(emp)
    notgoing=g(person)

    person.f=max(going,notgoing)     # biore lepsza opcje w zaleznosci czy idzie czy nie
    return person.f

def g(person):      # najlepsza impreza na ktora nie idzie person
    if person.g>=0:
        return person.g
    # to samo co suma najlepszych imprez na ktore ida bezposredni podwladni person
    best=0
    for emp in person.emp:
        best+=f(emp)
    person.g=best
    return best

def who(arr):           #tablica w ktorej sa osoby(poziomami od gory i od lewej)
    participants=[]
    idx=0 # zaczynam od bossa
    while idx<len(arr):
        person=arr[idx]
        # jezeli wartosc f jest wieksza od g, tzn ze lepiej bylo go wziac niz nie
        if person.f>person.g :
            person.going=True           # on idzie
            idx+=1
            for emp in person.emp:
                emp.going=False         # bo to podwladni tego co idzie
                idx+=1                  # przesuwam sie aby wiedziec kiedy skoncza sie osoby (petla wykonuje sie znow)
        else:
            person.going=False          # nie idzie
            idx+=1
            for emp in person.emp:
                if emp.f>emp.g :        #bierzemy podwladnych ale tylko pod warunkiem ze lepiej ich wziac nie nie
                    emp.going=True
                    idx+=1
                else:
                    emp.going=False
                    idx+=1

    # biore tylko tych ktorzy maja True    
    for el in arr:
        if el.going==True:
            participants.append(el.name)
    return participants
    



# tworze obiekty (osoby)

a=Person('Franek',3)
b=Person('Basia',5)
c=Person('Sylwia',2)
d=Person('Karol',5)
# reszta nie ma podwladnych
e=Person('Kornel',4)
f1=Person('Monika',3)
g1=Person('Kuba',6)
h=Person('Kacper',2)
i=Person('Maria',6)
a.emp=[b,c,d]
b.emp=[e]
c.emp=[f1,g1]
d.emp=[h,i]

arr=[a,b,c,d,e,f1,g1,h,i] #mam cale drzewo w tablicy (od gory wierszami (i od lewej)

print("fun: ",f(a))
print("\nparticipants: ",who(arr),"\n")

for i in [a,b,c,d,e,f1,g1,h,i]:
    print(i.name,"\t",i.going,"\t",i.fun,i.f,"\t",i.g,"\t","podwladni: ",len(i.emp))
