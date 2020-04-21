def sort(tab):

    for i in range(len(tab)):
        min=i 
        
        for j in range(i+1,len(tab)):
            if(tab[j]<tab[min]): min=j
            
        tab[i],tab[min]=tab[min],tab[i]
