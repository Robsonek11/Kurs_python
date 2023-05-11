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