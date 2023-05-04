
# 1▹ Stwórz listę przedmiotów, które zabierzesz na samotną wyprawę w góry. Elementy na liście posortuj alfabetycznie, a następnie wyświetl.
#zad1
items = ["headphones", "apple", "phone", "water"]

items.sort()

for elem in items:
    print(elem, '!')
# 2▹ Pobierz od użytkownika 10 liczb, wyświetl tylko te, które są nieparzyste.
#Zad2
tablica = []
numbers = int(input("ile elementów chcesz podać ->"))
tablica2 =[]
for _ in range(numbers):
    item = input("Podaj element, który chcesz dodać do listy -> ")
    tablica.append(item)

print(tablica)

for i in tablica:
    if int(i) % 2 == 0:
        tablica2.append(i)
print("Parzyste liczby tablicy to :",tablica2)

# 3▹ Dla podanej przez użytkownika liście liczb całkowitych sprawdź czy pierwszy i ostatni element są takie same.
#Zad3
arr = []
num = int(input("ile elementów chcesz podać ->"))

for _ in range(num):
    item = input("Podaj element, który chcesz dorzucic do list ->")
    arr.append(item)

print(arr)

print(arr[0])
print(arr[-1])

if arr[0] == arr[-1]:
    print('Elementy są takie same')
else:
    print('Elementy nie są takie same')

# 4▹ Pobierz od użytkownika parzystą listę elementów. Sprawdź czy 2 środkowe elementy są takie same.
#Zad4

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



# 5▹ Utwórz “na sztywno” 2-wymiarową tablicę, tak, by kolejne wiersze zawierały dane osób, natomiast w kolumnach będzie znajdować się imię, nazwisko, zawód, np:

#
#     Dorota, Wellman, dziennikarka
#
#     Adam, Małysz, sportowiec
#
#     Robert, Lewandowski, piłkarz
#
#     Krystyna, Janda, aktorka
#
# Wyświetl w sposób przyjazny dla użytkownika
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