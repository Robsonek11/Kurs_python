num = int(input("ile elementów chcesz podać ->"))
tab=[]

for _ in range(num):
    item = input("Podaj element, który chcesz dorzucic do list ->")
    tab.append(item)

print(tab)
print(type(tab))
i = 0
najwieksza = None
print(najwieksza)
for i in tab:
    if najwieksza==None or najwieksza < i:
        najwieksza = i
        print(najwieksza)

print("największa liczba to:", najwieksza)