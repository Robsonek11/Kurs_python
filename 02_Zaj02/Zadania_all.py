#Zad1
#Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem (np.jako jeden string rozdzielonych przecinkiem lub białym #znakiem). Następnie powitaj każdą osobę na liście.
arr =str(input('Podaj listę słów po spacji '))
arr2 = arr.replace(" ", ",").split(',')
arr3 = list(arr2)
#arr2 = arr.split
print(arr3)
for i in arr3:
    print('Hello ', i)
#Zad2
#Pobierz od użytkownika dowolny tekst i wyświetl tylko te znaki, które są na pozycjach parzystych. Wykonaj na dwa sposoby - za #pomocą pętli oraz przez sting slicing ( ‘abrakadabra’ -> ‘baaar’).
txt = str(input('Podaj dowolny tekst '))
print(txt[1::2])
txt1=list(txt)

for id in txt1[1::2]:
    print (id, end="")
#Zad3
#W podanym przez użytkownika ciągu wejściowym policz wszystkie małe litery, wielkie litery, cyfry i znaki specjalne.
txt = input('Podaj dowolny ciąg znaków ')
lower_letters = 0
upper_letters = 0
digits = 0
others_chars = 0

for i in txt:
    if i.isupper():
        upper_letters +=1
    elif i.islower():
        lower_letters +=1
    elif i.isdigit():
        digits +=1
    else:
        others_chars +=1


print('Lower leters: ', lower_letters)
print('Upper leters: ', upper_letters)
print('Digits: ',digits)
print('Others: ',others_chars)

#Zad4
#Napisz grę - kamień (k) / papier (p) / nożyce (n).

        #Użytkownik podaje jedną z 3 figur.

        #Komputer losuje jedną z 3 figur.

        #Sprawdź kto wygrał tę rundę.

        #Zmień kod tak, by użytkownik mógł podac liczbę rund.

        #Wygrana jest podawana jako suma wygranych rund komputer vs użytkownik.

        #Zmień tak, by gracz mógł zakończyć grę w dowolnej chwili przez np. hasło ‘koniec’

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



#Zad5
#Stwórz grę ciepło zimno.

       # Komputer losuje liczbę z zakresu od 1 do 100.

       # Użytkownik podaje swój traf.

       # Komuter odpowiada ciepło zimno, ale nie więcej niż 6 razy.

       # Jeśli użytkownik zgadnie wygrywa gracz.

       # Jeśli po 6 próbach użytkownik nie zgadnie - wygrywa komputer.

import random
select_komp = random.randrange(1, 100)
print (select_komp)
answer = -1
i = 1
print ("Zgadnij liczbę z przedziału (0,100): ")
print ('Masz 6 prób')
while i < 7:

    print ('Krok:', i)
    i += 1
    answer = int(input('Podaj liczbę: '))
    if answer < select_komp:
        print('        Niestety wylosowana liczba jest wieksza od Twojej')
    elif answer > select_komp:
        print('        Niestety wylosowana liczba jest mniejsza od Twojej')
    if answer == select_komp:
        print ('Brawo odgadłeś liczbę')
        break
    if i == 7:
        print ('Przykro mi  nieodgadłeś liczby w 6 krokach')
        break