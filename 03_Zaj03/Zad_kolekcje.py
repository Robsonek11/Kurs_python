# zad1
import random
tab=[]
number = int(input('Podaj liczbę losowanych liczb '))
for i in range(number):
    x = random.randrange(1, 100)
    tab.append(x)
print(tab)
krotka = tuple(tab)
dl_krotka = len(krotka)
print(dl_krotka)
unikalne = set(krotka)
print(unikalne)
dl_set = len(unikalne)
print(dl_set)

# zad2
# 2▹ Utwórz listę L_test = [1, 2, 3, 4], krotkę T_test = (1, 2, 3, 4) oraz set S_test = {1, 2, 3, 4}. Jakie metody dostępne dla typu list nie będą działać dla typów tuple i set?


L_test = [1, 2, 3, 4]
T_test = (1, 2, 3, 4)
S_test = {1, 2, 3, 4}

L_test.append("5")
# T_test.append("5")
# S_test.append("5")
print(L_test)
print(T_test)
print(S_test)

L_test.append("5")
# T_test.append("5")
# S_test.append("5")
print(L_test)
print(T_test)
print(S_test)

L_test.extend(T_test)
print(L_test)
print(T_test)
print(S_test)

# Działa len(), max(), min(), sum(), any(), all(), sorted(), count(), index()
# Nie działa append(), clear(), copy(), extend(), index(), insert(), pop(), remove(), reverse(), sort()

# Zad3
# 3▹ Utwórz 2 krotki. Następnie utwórz listę będącą połączeniem elementów o parzystym indeksie z pierwszej krotki, a oraz nieparzystych elementów z drugiej. Przekształć powstałą listę w set.

arr = []
arr1 = []
num = int(input("ile elementów chcesz podać ->"))

for _ in range(num):
    item = input("Podaj element, który chcesz dorzucic do listy1 ->")
    arr.append(item)

print(arr)

num = int(input("ile elementów chcesz podać ->"))

for _ in range(num):
    item = input("Podaj element, który chcesz dorzucic do listy2 ->")
    arr.append(item)
print(arr1)
krotka1 = tuple(arr)
krotka2 = tuple(arr1)

tuples_to_list = list(krotka1[:: 2] + krotka2[1:: 2])

print(tuples_to_list)
list_to_set = set(tuples_to_list)
print(list_to_set)

# zad4
import random

tab = []
number = int(input('Podaj liczbę losowanych liczb jako wielokrotność cyfry trzy '))
if number % 3 == 0:
    for i in range(number):
        x = random.randrange(1, 100)
        tab.append(x)
    print(tab)
    w = int(len(tab) / 3)
    tab1 = tab[0:w]
    tab2 = tab[w:2 * w]
    tab3 = tab[2 * w:]

    print("Tablica 1", tab1)
    tab1.reverse()
    print("Tablica 1", tab1)

    print("Tablica 2", tab2)
    tab2.reverse()
    print("tablica 2", tab2)

    print("Tablica 3", tab3)
    tab3.reverse()
    print("tablica 3", tab3)
else:

    print('Nie podałeś wielokrotności liczby 3')
# zad5
# 5▹ Porównaj zachowanie discard() vs remove() dla typu set.

set1 = {1, 2, 3, 4, 5, 6}
print(set1)
set1.discard(7)
print(set1)
set1.remove(7)
print(set1)

# remove zgłasza błąd gdy elementu nie ma
