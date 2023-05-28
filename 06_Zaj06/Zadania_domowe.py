#Zad1
# Utwórz plik zawierający listę ok. 20 cytatów. Każdy cytat powinen się znaleźć w nowej linii. Utwórz funkcję, która losuje i wyświetla w sposób ciekawy cytat na dziś.
# Np. można wyświetlić tak:
import random
def plik():
    nazwa = input('Podaj nazwę pliku ')
    return nazwa
def haslo_dnia(nazwa):

    with open(f'{nazwa}.txt', encoding='utf-8') as fopen:
        content = fopen.readlines()

        cytat = random.choice(content)
        txt, autor = cytat.split('[')
        autor = autor.replace(']',"")
        print('Quote of the day is:')
        print()
        width = 70
        print('*' * width)
        print(txt.center(width))
        print(autor.strip().center(width))
        print('*' * width)
def main():
    nazwa1 = plik()
    nazwa = nazwa1
    haslo_dnia(nazwa)
main()


#Zad2
# Zapoznaj się z modułem os. Sprawdź rozmiar utworzonego przez siebie pliku.
import os
os.path.getsize("example1.txt")
print(os.path.getsize("example1.txt"))

#Zad3
#3▹ Wyświetl tylko 5 pierwszych linii
def get_content():
    filename = input('Podaj nazwe pliku (bez rozszerzenia txt)')
    with open(f'{filename}.txt', encoding='utf-8') as fopen:
        content = fopen.readlines()

    return content

def main():
    quotes = get_content()

    print(quotes[0:5])
    for i in quotes[0:5]:
        print(i)
main()
#Zad4
# 4▹ Wyświetl 3 losowe cytaty


import random


def get_content():
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename

    Tk().withdraw()  # Ukrycie głównego okna aplikacji

    # Wyświetlenie okna dialogowego do wyboru pliku
    file_path = askopenfilename()

    # Otwarcie wybranego pliku w trybie odczytu
    with open(file_path, 'r', encoding='utf-8') as file:
        # Wykonaj operacje na pliku
        content = file.readlines()
    return content

def show(quote):
    print('Quotes of the day is:')
    print()
    width = 60
    print('*' * width)
    for i in quote:
        print(i.strip().center(width))
    print('*' * width)


def main():
    quotes = get_content()
    quote=random.choices(quotes, k = 3)

    show(quote)


main()


#Zad5
# Wykorzystaj plik zawierający fragment Pana Tadeusza.
# Znajdź najdłuższe słowo występujące w zadanym fragmencie.
def get_content():

    with open('pan_tadzio.txt', encoding='utf-8') as fopen:
        content = fopen.read()

    return content
def main():
    quotes = get_content()


    quotes = quotes.replace(',','').replace(')',"").replace('!',"").split()
    print(quotes)
    max_slowo= []
    for i in quotes:
        if len(i) > len(max_slowo):
            max_slowo=i
    print(f'Najdłużse słowo to: {max_slowo}')
    return
#zad6
# Rozpoznawanie kart. Utwórz plik zawierający numery kart kredytowych.
# Sprawdź dla każdej kart jej typ. Podziel kart do plików wg typów np. visa.txt,
# mastercard.txt, americanexpress.txt.

# Rozpoznawanie kart. Utwórz plik zawierający numery
# kart kredytowych. Sprawdź dla każdej kart jej typ.
# Podziel kart do plików wg typów
# np. visa.txt, mastercard.txt, americanexpress.txt.


def get_card_number():
    with open('visa.txt', 'r') as visa, open('mastercard.txt', 'r') as mastercard, open('americanexpres.txt','r') as americanexpress:
        lines = (visa or mastercard or americanexpress)
        print(lines)
        for number in visa.readlines() and mastercard.readlines() and americanexpress.readlines():
            card_nr = number
            card_nr = card_nr.replace(" ", "")
            card_nr = card_nr.replace("-", "")
            print(card_nr)

        return card_nr


def is_visa(card_num):
    """Function that checks visa numbers"""
    return card_num[0] == '4' and (len(card_num) == 16 or len(card_num) == 13)
    # if card_num[0] == '4' and (len(card_num) == 16 or len(card_num) == 13):
    #     return True
    # else:
    #     return False


def is_mastercard(card_num):
    """Function that checks mastercard numbers"""
    start_condition = int(card_num[0:2]) in range(51, 56) or int(card_num[0:4]) in range(2221, 2721)

    return len(card_num) == 16 and start_condition
    # if len(card_num) == 16 and start_condition:
    #     return True
    # else:
    #     return False


def is_amex(card_num):
    """Function that checks amex numbers"""
    return len(card_num) == 15 and card_num[0:2] in ('34', '37')
    # if len(card_num) == 15 and card_num[0:2] in ('34', '37'):
    #     return True
    # else:
    #     return False


def main():
    number = get_card_number()
    print('💳 :', number)

    if is_visa(number):
        print("This is Visa card number")
    elif is_mastercard(number):
        print("This is MasterCard card number")
    elif is_amex(number):
        print("This is AmericanExpress card number")
    else:
        print("Unknown card number")



main()



