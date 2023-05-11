# 5▹ Stwórz grę ciepło zimno.
#
#         Komputer losuje liczbę z zakresu od 1 do 100.
#
#         Użytkownik podaje swój traf.
#
#         Komuter odpowiada ciepło zimno, ale nie więcej niż 6 razy.
#
#         Jeśli użytkownik zgadnie wygrywa gracz.
#
#         Jeśli po 6 próbach użytkownik nie zgadnie - wygrywa komputer.

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