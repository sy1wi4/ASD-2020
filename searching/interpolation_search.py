#wyszkukiwanie proporcjonalne(interpolacyjne)


def search(tab, x): 
    p=0
    k=len(tab)-1
   
    while p <= k and x >= tab[p] and x <= tab[k]: 
        if p==k: 
            if tab[p] == x :  
                return p; 
            return -1; 
          
        
        pos  = p + int(((float(k-p) / ( tab[k]-tab[p])) * ( x - tab[p])))
        
        if (tab[pos]==x): 
            return pos 
   
        if tab[pos] < x : 
            p = pos + 1; 
    
        else: 
            k = pos - 1; 
      
    return -1
