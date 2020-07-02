import math

def size(k): return k[0]

def level(i): return int(math.log2(i))

def heapifyMin(k,i):
    left=2*i
    right=2*i+1
    Min=i
    #spr dzieci i, wiem ze jedno jest na pewno
    child=True
    if(left<=size(k) and k[left]<k[Min]): 
        Min=left
    if(right<=size(k) and k[right]<k[Min]): 
        Min=right
    for j in range (4*i,i*4+4):  #spr wnuki, jesli sa (od i*4 do i*4+3 wlacznie)
        if(j<=size(k) and k[j]<k[Min]):
            Min=j
            child=False
    if (child and Min!=i):
        k[Min],k[i]=k[i],k[Min] #tylko zamieniam ojca z dzieckiem
    elif(child==False and Min!=i):   #jesli ma wnuki to na pewno ktorys jest mniejszy od dzieci, porownuje je z i
        #child jest false, to oznacza, ze mam jako Min wnuka, zamieniam go z i
        k[Min],k[i]=k[i],k[Min]
        #i sprawdzam czy teraz syn i nie jest mniejszy od swojego syna, jesli tak to zamieniam
        #oraz wywoluje ponownie - spr czy pod nim jest ok
        if (k[Min//2]<k[Min]):
            k[Min//2],k[Min]=k[Min],k[Min//2]
        heapifyMin(k,Min)

def heapifyMax(k,i):
    left=2*i
    right=2*i+1
    Max=i
    #spr dzieci i, wiem ze jedno jest na pewno
    child=True
    if(left<=size(k) and k[left]>k[Max]): 
        Max=left
    if(right<=size(k) and k[right]>k[Max]): 
        Max=right
    for j in range (4*i,i*4+3):  #spr wnuki, jesli sa (od i*4 do i*4+3 wlacznie)
        if(j<=size(k) and k[j]>k[Max]):
            Max=j
            child=False
    if (child and Max!=i):
        k[Max],k[i]=k[i],k[Max] #tylko zamieniam ojca z dzieckiem
    elif(child==False and Max!=i):   #jesli ma wnuki to na pewno ktorys jest mniejszy od dzieci, porownuje je z i
        #child jest false, to oznacza, ze mam jako Max wnuka, zamieniam go z i
        k[Max],k[i]=k[i],k[Max]
        #i sprawdzam czy teraz syn i nie jest wiekszy od swojego syna, jesli tak to zamieniam
        #oraz wywoluje ponownie - spr czy pod nim jest ok
        if (k[Max//2]>k[Max]):
            k[Max//2],k[Max]=k[Max],k[Max//2]
        heapifyMax(k,Max)       



def heapify(k,i):
    if(level(i)%2==0): return heapifyMin(k,i)    #jestem na min levelu(parzystym)
    else: return heapifyMax(k,i)


def buildHeap(k):
    for i in range(size(k)//2,0,-1):
        heapify(k,i)
    return k
    #budujemy tutaj odpowiedni kopiec min max(i-ty el na pewno ma dziecko,ale nie wiemy,czy wnukow)

def getMin(k):
    #najmniejszy jest na samej gorze
    res=k[1]
    k[1]=k[size(k)]  #ostatni daje na poczatek,zmiejszam rozmiar
    k[0]=k[0]-1
    heapify(k,1)
    return res

def getMax(k):
    #najwiekszy jest drugi lub trzeci element
    if(k[2]>=k[3]): 
        res=k[2]
        k[2]=k[size(k)]
    else: 
        res=k[3]
        k[3]=k[size(k)]
        k[0]=k[0]-1
    heapify(k,1)
    return res
