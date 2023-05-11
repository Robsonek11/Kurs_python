number_1 = int(input('Podaj liczbę pierwszą '))
number_2 = int(input('Podaj liczbę drugą '))
number_3 = int(input('Podaj liczbę trzecią '))

if number_1>number_2>number_3:
    print('Najwieksza liczba' , number_1)
    print(number_1, number_2, number_3)
elif number_2>number_1>number_3:
    print('Najwieksza liczba', number_2)
    print(number_2, number_1, number_3)
elif number_3 > number_1 > number_2:
    print('Najwieksza liczba', number_3)
    print(number_3, number_1, number_2)
elif number_1 > number_3 > number_2:
    print('Najwieksza liczba', number_1)
    print(number_1, number_3, number_2)
else:
    print('Najwieksza liczba', number_3)
    print(number_3, number_2, number_1)