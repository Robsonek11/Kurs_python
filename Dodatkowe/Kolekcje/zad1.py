# 1▹ Utwórz dowolną krotkę, w której elementy mogą się powtarzać. Przekształć ją w set.
#zad1
import random
tab=[]
number = int(input('Podaj liczbę losowanych liczb '))
for i in range(number):
    x = random.randrange(1, 100)
    tab.append(x)
print(tab)
krotka = tuple(tab)
dl_krotka= len(krotka)
print(dl_krotka)
unikalne = set(krotka)
print (unikalne)
dl_set = len(unikalne)
print(dl_set)

#


