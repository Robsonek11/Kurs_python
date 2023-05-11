#Zad4
#Pobierz od użytkownika parzystą listę elementów. Sprawdź czy 2 środkowe elementy są takie same.

tab = input('Podaj parzysta listę  słów z przecinkami ')
tab = tab.replace(" ", ",").split(',')
if len(tab)%2 != 0:
    print('Twoja tablica ma nieparzystą liczbe elementów')
    print(tab)
    print('Element środkowy', tab[int(len(tab) / 2)])
else:
    print('Twoja tablica ma parzystą liczbe elementów')
    print(tab)

    if tab[int(len(tab)/2-1)] == tab[int(len(tab)/2)]:
        print('Elementy środkowe', tab[int(len(tab) / 2 - 1)], "i", tab[int(len(tab) / 2)], 'są takie same')
    else:
        print('Elementy środkowe', tab[int(len(tab) / 2 - 1)], "i", tab[int(len(tab) / 2)], 'nie są takie same')
#Zad5
people = [
    ['Dorota', 'Wellman', 'dziennikarka'],
    ['Adam', 'Małysz', 'sportowiec'],
    ['Robert', 'Lewandowski', 'piłkarz'],
    ['Krystyna', 'Janda', 'aktorka']
]

# for row in people:
#     # print(row[0], row[1], '-', row[2])
#     print(" - ".join(row))

print('---------')


for person in people:
    for id, elem in enumerate(person):
        if id == 1:
            print(elem, end=" - ")
        else:
            print(elem, end=" ")
    print()