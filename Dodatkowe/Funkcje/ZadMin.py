# Nie korzystając z funkcji wbudowanej min(), napisz funkcję znajdującą minimalną
# wartość z 3  liczb.minimum_of(a, b, c).

arr=[]
i=0
najwieksza = 0
def minimum_of(najwieksza):
    for i in arr:
        print(i)
        if int(najwieksza) < int(i):
            najwieksza = i
    return najwieksza


num = int(input("ile elementów chcesz podać ->"))

for _ in range(num):
    item = input("Podaj element, który chcesz dorzucic do listy1 ->")
    arr.append(item)

print(f"najwieksza liczba w zbiorze {arr}, to {minimum_of(najwieksza)}")