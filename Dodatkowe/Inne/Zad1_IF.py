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

length = len