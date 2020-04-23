def binSearch(tab,val,p,k):
    if(p<=k):
        s=(p+k)//2
        if(tab[s]==val): return s
        elif(tab[s]>val): return binSearch(tab,val,p,s-1)
        else: return binSearch(tab,val,s+1,k)
    else: return None

