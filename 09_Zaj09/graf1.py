miejsca = [
'dom', 'szkoła', 'kościół', 'bar', 'szpital', 'kino', 'teatr'
]
macierz_sasiedztwa = [

    [0, 1, 1, 1, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 1, 1],
    [0, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 1, 0]
]

for wiersz in range(0, len(miejsca)):
    for kolumna in range(0, len(miejsca)):
        if macierz_sasiedztwa[wiersz][kolumna] == 1:
            print('Połączenie:',miejsca[wiersz], '->', miejsca[kolumna])