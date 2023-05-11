# 13.	Napisz program, który używa pętli while do odgadnięcia liczby
# wylosowanej przez komputer z zakresu od 1 do 100. Program powinien
# umożliwiać użytkownikowi wprowadzenie próby odgadnięcia i wyświetlić odpowiedni
# komunikat, czy liczba jest za duża, za mała czy poprawna.

import random
i = 1
j = 0
x = random.randrange(1, 100)
print(x)
number = 0
number = int(input('Podaj liczbę z zakresu od 1 do 100 '))
while x != number:
    if x > number:
        print('Twoja liczba jest za mała')
        number = int(input('Podaj liczbę z zakresu od 1 do 100 '))
        i = i + 1
    else:
        print('Twoja liczba jest za duża')
        number = int(input('Podaj liczbę z zakresu od 1 do 100 '))
        j = j + 1
if x == number:
    print(f"brawo odgadłeś liczbę w {i+j} krokach")
