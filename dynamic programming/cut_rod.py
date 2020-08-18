'''
Firma kupuje długie stalowe pręty i tnie je na kawałki, które sprzedaje. Kawałki mają długość w metrach
wyrażoną zawsze liczbą naturalną. Dla kawałka długości n metrów znane są ceny kawałków długości 1, 2, …, n
metrów. Firma chce znać maksymalny zysk, który może uzyskać z pocięcia i sprzedania pręta długości n.
'''

# w tablicy dp pod indeksem i trzymamy maksymalny zysk z pocięcia kawałka pręta o długości i, a w tablicy price
# mamy pod price[i] cenę kawałka długości i
# sprawdzamy coraz dłuższe pręty - "odcinamy" kawałek o długości j, a następnie odczytujemy zmaksymalizowany
# zysk z tablicy dp  - już wcześniej obliczony

def cut_rod(price,n):
    dp=[0]*(n+1)
    dp[1] = price[1]

    for length in range(2,n+1) :
        for j in range(1,length+1) :
            dp[length] = max(dp[length], price[j] + dp[length-j])
    print(dp)
    return dp[n]
