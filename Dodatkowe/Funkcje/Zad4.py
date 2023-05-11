# Napisać funkcję, która wypisze wszystkie parzyste z przekazanej listy elementów
# (wykorzystać funkcje z pkt 2)
arr1 = []
def even(arr1):

    for i in arr:
        if int(i) % 2 == 0:
            arr1.append(i)
    return arr1





arr = []
num = int(input("ile elementów chcesz podać ->"))

for _ in range(num):
    item = input("Podaj element, który chcesz dorzucic do listy1 ->")
    arr.append(item)

print(f" Twoje liczby {even(arr1)} są parzyste ")
