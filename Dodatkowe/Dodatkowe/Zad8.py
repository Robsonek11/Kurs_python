# 8.	Napisz program, który używa pętli for do zamiany miejscami dwóch elementów tablicy o
# określonych przez użytkownika indeksach.
num = int(input("ile elementów chcesz podać ->"))
arr = []
arr2 = []
for _ in range(num):
    item = int(input("Podaj element, który chcesz dorzucic do listy1 ->"))
    arr.append(item)

print(arr)
arr2 = arr
print(arr2)
number1 = int(input(f" Podaj indeksy od 1 do {len(arr2)}-> "))
number2 = int(input(f" Podaj indeksy od 1 do {len(arr2)}-> "))

# x = number1-1
# y = number2-1
# a = arr2[x]
# b = arr2[y]
# print(a)
# print(b)
# arr2.pop(x)
# arr2.insert(x, b)
# arr2.pop(y)
# arr2.insert(y, a)
# print(arr)
# print(arr2)

for i in