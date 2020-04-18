''' mamy tablice aktywnosci, kazda ma swoj start time i finish time, chcemy wybrac jak najwieksza ilosc kompatybilnych ze soba aktywnosci
[starttime, finishtime), tablica jest posortwonana wedlug finish time, ale jesli nie to sortujemy ja w taki wlasnie sposob'''

# 0 komorki nie bedziemy uzywac, tam pomocniszo start i finish to 0

class activity:
    def __init__(self,start,finish):
        self.start=start
        self.finish=finish


# nasza odp bedzie activitySekRek(arr,0) --> jako ostatni najpierw mam ten element ktory ma finish=0 (z 0 komorki)

def activitySelRec(arr,last,res):       # przekazujemy indeks elementu jaki wybralismy ostatnio
    n=len(arr)-1                        # ostatni element jaki jest w tablicy ma indeks n
    curIdx=last+1                       # element ktory bedziemy probowali dolaczac
    while (curIdx<=n and arr[curIdx].start<arr[last].finish):
        curIdx+=1
    if curIdx<=n:
        res.append(curIdx)
        return activitySelRec(arr,curIdx,res)+1
    else:
        return 0

    
def printAct(act):
    print("start:", act.start)
    print("finish", act.finish,"\n")

pom=activity(0,0)
a=activity(1,5)
b=activity(5,6)
c=activity(6,8)
d=activity(3,12)
e=activity(2,14)
f=activity(9,18)
g=activity(19,20)
arr=[pom,a,b,c,d,e,f,g]
res=[]
print("ilosc aktywnosci: ",activitySelRec(arr,0,res))
print(res)
