#1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987

def fib(n):
    if n<=2 : 
        return 1
    return fib(n-1)+fib(n-2)
    
def fibDP(n):     # sumujemy elementy tablicy
    F=[1]*(n+1)
    for i in range(3,n+1):
        F[i]=F[i-1]+F[i-2]
    return F[i]

def fibBetterDP(n):     # w zasadzie musimy pamietac tylko 2 poprzednie wyrazy
    Fo1=1       # wyraz poprzedni
    Fo2=1       # wyraz 2 wczesniej
    if(n<=2): return 1
    for _ in range(3,n+1):
        F=Fo1+Fo2
        Fo2=Fo1
        Fo1=F
    return F



def fibMemStack(n):
    F=[0]*(n+1) 
    F[1]=1
    F[2]=1
    stack=[None]*(2*n)
    top=0
    stack[top]=n
    while(top>=0):

        idx=stack[top]
        if(F[n]!=0): return F[n]
        elif F[idx]!=0 :
            stack[top]=None
            top-=1
            nextidx=stack[top]
            stack[top]=None
            top-=1
            F[idx+1]=F[idx]+F[nextidx]
        else:
            top+=1
            stack[top]=idx-2
            top+=1
            stack[top]=idx-1
        #print(stack,"\nF:\t ",F,"\n")
