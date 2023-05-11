# 1.	Napisz program, który pyta użytkownika o dwie liczby i wyświetla wynik ich mnożenia, ale tylko wtedy, gdy obie liczby są dodatnie. W przeciwnym wypadku wyświetl komunikat ”Nie mnożę!”

number1 = int(input('Padja liczbę '))
number2 = int(input('Padja liczbę '))

if number1 < 0 or number2 <0:
    print ('Nie mnoże')
else:
    wynik = number1 * number2
    print(f"Wynik mnożenia {wynik}")