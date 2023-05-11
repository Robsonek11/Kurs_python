number = int(input('Podaj liczbę->'))
if number %3 == 0:
    print("Twoja liczba jest podzielna przez3")
else:
    print("Twoja liczba niejest podzielna przez3")

op1 = int(input('podaj opinię 1 (1-10)->'))
op2 = int(input('podaj opinię 2 (1-10)->'))
op3 = int(input('podaj opinię 2 (1-10)->'))
average = (op1+op2+op3)

if average >= 7:
    print("Bardzo dobry ")
elif average >=4:
    print("nie interesująca")
else:
    print("Zły ")


password = "Tajne haslo"
# Stwórz zmienną password. Hasło powinno składać z liter i cyfr,
# zwierać conajmniej 1 małą literę,
# 1 dużą literę i mieć długość conajmniej 8 znaków,
# Poinformuj użytkownika, jeśli wpisane hasło jest nie poprawne.
# Wyświetl różne komunikaty w zależności od rodzaju błędu

password = "Tajne haslo1"

# jesli za krótkie
if len(password) < 8:
    print('Password too short')
# jesli nie ma cyfry
if password.isalnum() and password.isalpha():
    print('Password needs at least one digit')
# jesli nie ma litery
if password.isalnum() and password.isdigit():
    print('Password needs at least one letter')
# jesli nie ma małej litery
if password.islower():
    print('Password needs at least 1 lower letter')
# jeśli nie ma dużej litery
if password.isupper():
    print('Password needs at least 1 upper letter')

print(f'super [not] secure password here -> {password}')