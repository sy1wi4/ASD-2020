'''
class field:
    def __init__(self,value,short,long):
        self.value=value
        self.short=short
        self.long=long

Z każdego pola można skakać tylko o ilość pól zapisaną w short lub long. Napisać program
który zwróci maksymalną wartość jaką możemy osiągnąć poprzez przejście z pola 0 do n-1.
Można założyć że z każdego pola da się dojść do pola n-1.
'''

# ALGORYTM:
'''
W tablicy dp[i] oznacza maksymalną osiągalną wartość z pola i-tego do końca.
Idziemy od końca tablicy i dla kolejnych pól decydujemy, czy lepiej
skoczyć o long czy short. Szukana wartość to dp[0].
'''

class field:
    def __init__(self,value,short,long):
        self.value=value
        self.short=short
        self.long=long


def max_value(arr):
    n=len(arr)
    dp=[0]*len(arr)
    dp[n-1]=arr[n-1].value

    for i in range(n-2,-1,-1):
    # decyzja czy lepiej skoczyć z aktualnej pozycji o long czy short
    # (skoro da się dojść do n-1 z każdego pola, tzn że short nie wyjdzie poza tablicę)
        dp[i]=dp[i+arr[i].short] + arr[i].value
        if i + arr[i].long < n :
            dp[i]=max(dp[i],dp[i+arr[i].long]+arr[i].value)

    return dp[0]
