#zad1
#Poproś użytkownika o podanie liczby. Sprawdź czy liczba podana przez użytkownika jest podzielna przez
#3 bez reszty i wyświetl komunikat “Twoja liczba jest podzielna przez 3”.

number = int(input('Podaj liczbę? '))
x = number % 3
if x == 0:
    print('Liczba jest podzielna przez 3')
else:
    print('Liczba nie jest podzielna przez 3')

#zad2
#Pobierz dwie liczby całkowite od użytkownika i oblicz ich sumę. Jeśli suma jest większa niż 100,
#wyświetl wynik, w przeciwnym wypadku wyświetl “Koniec”.
number_one = int(input('Podaj liczbę 1? '))
number_two = int(input('Podaj liczbę 2? '))
sum = number_one+number_two

if sum >100:
    print('Suma wynosi ', sum)
else:
    print('Koniec')
#Zad3
#Stwórz skrypt, który przyjmuje 3 opinie użytkownika o książce. Oblicz średnią opinię o książce.
#W zależności od wyniku dodaj komunikaty. Jeśli uzytkownik ocenił książkę na ponad
#7 - bardzo dobry, ocena 5-7 przeciętna, 4 i mniej - nie warta uwagi.

view_1 = int(input('Podaj oponie nr1 (0-10 )' ))
view_2 = int(input('Podaj oponie nr2 (0-10 )' ))
view_3 = int(input('Podaj oponie nr3 (0-10 )' ))

mean = (view_1+view_2+view_3)/3

if mean >7:
    print('Bardzo dobra ksiązka')
if mean <4:
    print ('Nie warta uwagi')
else:
    print('Przeciętna książka')

#Zad4
# Utwórz zmienną przechowującą dowolny ciąg znaków. Sprawdź czy utworzony string jest dłuższy
# niż 5 znaków oraz czy zawiera literę a. Jeśli zawiera, wszystkie litery a podmień na z i wyświetl
#powstały napis.

txt = str(input('Podaj wyraz '))
if len(txt) > 5 and txt.find('a'):
    txt_i = txt.replace('a', 'i')
    print(txt_i)
else:
    print('Twój wyraz ma mniej niż 5 liter')

#Zad5
#Stwórz zmienną password. Hasło powinno składać z liter i cyfr, zwierać conajmniej 1 małą literę,
# 1 dużą literę i mieć długość #conajmniej 8 znaków. Poinformuj użytkownika, jeśli wpisane hasło
# jest nie poprawne. Wyświetl różne komunikaty w zależności od rodzaju błędu.

password = str(input('Podaj hasło '))

length = len(password)
lower = password.islower()
digit = password.isalpha()
numeric = password.isalnum()
big = password.isupper()
#print ('Digit', digit)
#print('alafa nume',numeric)
if length < 8:
    print('Twoje hasło jest zakrótkie')
if lower == True:
    print('Twoje haslo nie ma duzej litery')
if big == True:
    print ('Nie ma małej litery')
if digit == True and numeric == True:
    print("Twoje hasło nie ma cyfry")
if numeric == True:
    print('Twoje hasło nie ma zanku alfanumerycznego')
else:
    print('Dobre hasło')

#Zad6
#Zapytaj użytkownika o numer od 1 do 100, jeśli użytkownik zgadnie liczbę ukrytą przez programistę wyświetl komunikat #“gratulacje!”, w przeciwnym razie wyświetl “pudło!”.

number = int(input("Podaj liczbę "))

if number == 36:
    print('Gratulacje')
else:
    print ('Próbuj dalej')
#Zad7
#Rozwiń kod bmi.py z pierwszych zajęć dodając teraz instrukcję warunkową, która wyświetli w zależności od wyniku: niedowaga / #waga normalna / nadwaga / otyłość.
w = input("Podaj wagę ->")
h = input("Podaj wzrost (w metrach) ->")

w = float(w.replace(",", "."))
h = float(h.replace(",", "."))

bmi = w / (h ** 2)
print (bmi)
if bmi < 15.99:
    print("Twoje BMI to \"wygłodzenie\":", round(bmi, 2))
elif bmi > 16 and bmi < 16.99:
    print("Twoje BMI to \"wychudzenie\":", round(bmi, 2))
elif bmi > 17 and bmi < 18.49:
    print("Twoje BMI to \"niedowaga\":", round(bmi, 2))
elif bmi > 18 and bmi <24.99:
    print("Twoje BMI jest \"optymalne\":", round(bmi, 2))
elif bmi > 25 and bmi < 29.99:
    print("Twoje BMI to \"nadwaga\":", round(bmi, 2))
elif bmi > 30 and bmi < 34.99:
    print("Twoje BMI to \"otyłość I st\":", round(bmi, 2))
elif bmi > 35 and bmi < 39.99:
    print("Twoje BMI jest \"otyłość II st\":", round(bmi, 2))
else:
    print("Twoje BMI jest \"otyłość III st\":", round(bmi, 2))

#Zad8
#Sortowanie. Trzy dowolne liczby podane przez użytkownika zapisz do trzech zmiennych. Znajdź największą liczbę. Wyświetl liczby #od największej do najmniejszej.

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
