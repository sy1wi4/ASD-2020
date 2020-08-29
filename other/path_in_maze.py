'''
Dana jest macierz binarna NxN. Chcemy znaleźć długośc *NAJKRÓTSZEJ* ścieżki z M[0][0]
do  M[x][y], dla danych i oraz j. Możemy się poruszać we wszystkich kierunkach, tylko po komórkach
o wartości 1 .
'''

# (zwykła rekurencja)



def shortest_path(M,i,j,x,y,current_dist,min_dist,visited):
    n = len(M)

    # warunek końca 
    if i == x and j == y :
        return min(min_dist,current_dist)

    visited[i][j] = True

    # pomocnicza funkcja, mówiąca, czy do danej komórki możemy iść - czy nie wychodzi poza tablicę,
    # czy wartość wynosi 1 i czy nie została już uprzednio odwiedzona 

    def is_ok(M,visited,i,j) :
        return i >= 0 and j >= 0 and i < n and j < n and M[i][j] == 1 and not visited[i][j] 

    if is_ok(M,visited,i+1,j) :

        min_dist = shortest_path(M,i+1,j,x,y,current_dist+1,min_dist,visited)

    if is_ok(M,visited,i,j+1) :

        min_dist = shortest_path(M,i,j+1,x,y,current_dist+1,min_dist,visited)

    if is_ok(M,visited,i-1,j) :

        min_dist = shortest_path(M,i-1,j,x,y,current_dist+1,min_dist,visited)

    if is_ok(M,visited,i,j-1) :

        min_dist = shortest_path(M,i,j-1,x,y,current_dist+1,min_dist,visited)

    # gdy wracamy, to odznaczamy komórkę z powrotem jako nieodwiedzona
    visited[i][i] = False

    return min_dist


M=[
    [1,1,1,1],
    [0,0,1,1],
    [0,1,1,0],
    [0,0,0,0]
]

# tworzymy tablicę, w której odznaczamy odwiedzone komórki, by nie zapętlić się
visited=[[False]*len(M) for _ in range(len(M))]

# przykładowe wywołanie
print(shortest_path(M,0,0,2,2,0,float("inf"),visited))
