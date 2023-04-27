#Zad1
#Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem (np.jako jeden string rozdzielonych przecinkiem lub białym #znakiem). Następnie powitaj każdą osobę na liście.

#Zad2
#Pobierz od użytkownika dowolny tekst i wyświetl tylko te znaki, które są na pozycjach parzystych. Wykonaj na dwa sposoby - za #pomocą pętli oraz przez sting slicing ( ‘abrakadabra’ -> ‘baaar’).

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
#Ważne

#Przed zadaniami 4 i 5 zapoznaj się z dokumentacają modułu random. Na początku pliku musisz dodać:

#import random

#Szczególnie zwróć uwagę na funkcje random.randint(), random.randrange() i random.choice().

#Zad4
#Napisz grę - kamień (k) / papier (p) / nożyce (n).

        #Użytkownik podaje jedną z 3 figur.

        #Komputer losuje jedną z 3 figur.

        #Sprawdź kto wygrał tę rundę.

        #Zmień kod tak, by użytkownik mógł podac liczbę rund.

        #Wygrana jest podawana jako suma wygranych rund komputer vs użytkownik.

        #Zmień tak, by gracz mógł zakończyć grę w dowolnej chwili przez np. hasło ‘koniec’

#Zad5
#Stwórz grę ciepło zimno.

       # Komputer losuje liczbę z zakresu od 1 do 100.

       # Użytkownik podaje swój traf.

       # Komuter odpowiada ciepło zimno, ale nie więcej niż 6 razy.

       # Jeśli użytkownik zgadnie wygrywa gracz.

       # Jeśli po 6 próbach użytkownik nie zgadnie - wygrywa komputer.

