names = input("Names: ").replace(",", " ").split(" ")
for i in names:
    print("Hello", i)

liczba = int(input("Podaj liczbę : "))

if liczba >8:
    print("Podaj liczbę pomiędzy 1 a 8:")
else:
    print(liczba, "! = ")

    silnia = 1

    for num in range(1, liczba+1):
        silnia = silnia * num
        print( num,"* ", end="")

    print(f" = {silnia}")
    print(f"Silnia z {liczba} wynosi {silnia}")
