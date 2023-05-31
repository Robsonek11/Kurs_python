#1
items = ["latarka", "słuchawki", "woda", "aplle"]
items.sort()
for i in items:
    print(i,"!")

#3
# --- opcja 1 ----
# arr = input('Podaj listę słów po spacji')
# # arr = arr.replace(" ", "").split(',')
# # arr = list(arr)
# arr = arr.split
# print(arr)

# --- opcja 2 ----
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
#5
list_2d =[["Dorota", "Wellman","dziennikarka"]],["Adam", "Małysz", "sportowiec"],["Robert", "Lewandowski", "piłkarz"],['Krystyna', "Janda", "aktorka"]
print(list_2d[1,2])