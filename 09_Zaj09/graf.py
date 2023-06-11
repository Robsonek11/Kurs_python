# # lista krotek - wierzchołki będą niemodyfikowalne
# graph = [(0, 1), (0, 2), (0, 3), (1, 0), (1,2), (2, 0), (2, 1), (2, 3), (3,0), (3,2)]
#
# # lista krotek - lista par na listach - wierzchołki modyfikowalne
# graph = [[0, 1], [0, 2], [0, 3], [1, 0], [1,2], [2, 0], [2, 1], [2, 3], [3,0], [3,2]]




wierzcholki = ['dom','szkola','kosciol','bar','szpital','kino','teatr']

macierz=[
[1,1,1,1,0,0,0],
[1,1,0,0,1,0,0],
[1,0,1,1,0,1,0],
[1,0,1,1,1,0,0],
[0,1,0,1,1,1,1],
[0,0,1,0,1,1,1],
[0,0,0,0,1,1,1],
]

def main():
    for row in macierz:
        i = 0
        while i < len(row):
            if row[i] == 1:
                print(f'{wierzcholki[macierz.index(row)]} -> {wierzcholki[i]}')
            i += 1
main()