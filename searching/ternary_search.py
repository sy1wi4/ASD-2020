def search(tab,x):
    p=0
    k=len(tab)-1
    while(p<=k):
        mid1=p+(k-p)//3
        mid2=k-(k-p)//3
        if(tab[mid1]==x): return mid1
        elif(tab[mid2]==x): return mid2
        if(x<mid1):
            k=mid1-1
        elif(x>mid2):
            p=mid2+1
        else:
            p=mid1+1
            k=mid2-1
    return -1
