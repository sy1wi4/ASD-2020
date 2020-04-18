''' mamy tablice aktywnosci, kazda ma swoj start time i finish time, chcemy wybrac jak najwieksza ilosc kompatybilnych ze soba aktywnosci
[starttime, finishtime), tablica jest posortwonana wedlug finish time, ale jesli nie to sortujemy ja w taki wlasnie sposob'''


class activity:
    def __init__(self,start,finish):
        self.start=start
        self.finish=finish

def activitySelector(arr):
    n=len(arr)
    res=[arr[0]]    # tablica wynikowa
    act=arr[0]      # aktualna aktywnosc
    i=1        #i-ty element chce dolaczyc
    while(i<n):
        while (i<n and arr[i].start<act.finish):        # szukam elementu, ktory moge dolaczyc
                i+=1
       
        if i<n :       
            res.append(arr[i])
            act=arr[i]
            i+=1
    return res
    
def printAct(act):
    print("start:", act.start)
    print("finish", act.finish,"\n")


a=activity(1,5)
b=activity(4,7)
c=activity(6,10)
d=activity(9,12)
e=activity(2,16)
f=activity(15,18)
g=activity(13,20)
arr=[a,b,c,d,e,f,g]
arr1=activitySelector(arr)
print("\nmax kompatybilnych aktywnosci: ")
for i in arr1:
    printAct(i)
