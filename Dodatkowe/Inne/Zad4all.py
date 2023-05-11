import random
print()
print()
print("-------------------------------------------------------------------------------------------")
number = int(input("Podaj liczbę rund..."))


print()
x = 0
y = 0
temp = number
temp = temp - number + 1
while number > 0:
    print("-------------------------------------------------------------------------------------------")
    print("runda ", temp)

    select = int(input("Wybierasz:\n1.Papier\n2.Kamień\n3.Nożyce\n -Wybrana Cyfra-......... "))
    print()
    print()
    number = number - 1
    temp=temp+1
    if select == 10:
        sys.exit(0)
    if select == 1:
        print('Twój wybór Papier')
    if select == 2:
        print('Twój wybór Kamień')
    if select == 3:
        print('Twój wybór Nożyce')
    select_komp = random.randrange(1, 3)

    if select_komp == 1:
        print('Wylosowany przez komputer Papier')
    if select_komp == 2:
        print('Wylosowany przez komputer Kamień')
    if select_komp == 3:
        print('Wylosowany przez komputer Nożyce')


    if select == 1 and select_komp == 1:
        print("Papier vs Papier")
        print("Remis!")

    if select == 2 and select_komp == 2:
        print("Kamień vs Kamień")
        print("Remis!")

    if select == 3 and select_komp == 3:
        print("Kamień vs Kamień")
        print("Remis!")

    if select == 1 and select_komp == 2:
        print("Papier vs Kamień")
        print("Wygrywasz!")
        x =x + 1
    elif select == 2 and select_komp == 3:
        print("Kamień vs Nożyce")
        print("Wygrywasz!")
        x = x + 1

    elif select == 3 and select_komp == 1:
        print("Nożyce vs Papier")
        print("Wygrywasz!")
        x = x + 1
    if select == 1 and select_komp == 3:
        print("Papier vs Nożyce")
        print("Przegrywasz!")
        y = y + 1
    elif select == 2 and select_komp == 1:
        print("Kamień vs Papier")
        print("Przegrywasz!")
        y = y + 1
    elif select == 3 and select_komp == 2:
        print("Nożyce vs Kamień")
        print("Przegrywasz!")
        y = y + 1
    print('Jest ',x,'do',y)

    z = str(input('Jeśli zechcesz zakończyć grę wpisz \"koniec"'))
    if z == "koniec":
        break