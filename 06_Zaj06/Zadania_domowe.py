#Zad1
# Utwórz plik zawierający listę ok. 20 cytatów. Każdy cytat powinen się znaleźć w nowej linii. Utwórz funkcję, która losuje i wyświetla w sposób ciekawy cytat na dziś.
# Np. można wyświetlić tak:
import random
def plik():
    nazwa = input('Podaj nazwę pliku (quote)')
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
    filename = input('Podaj nazwe pliku (bez rozszerzenia txt(cytaty))')
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
    with open('06.karty/visa.txt', 'r') as visa, open('06.karty/mastercard.txt', 'r') as mastercard, open(
            '06.karty/americanexpres.txt', 'r') as americanexpress:
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




# 7▹ Wisielec.
#  Utwórz plik zawierający listę słów wg.
# kategorii np. zwierzęta, owoce etc. (jedna linia po przecinku)
#
# Poproś użytkownika o
# podanie kategorii przed rozpoczęciemy gry.
#  1 - zwierzeta
#  2 - owoce
#  3 - warzywa
#
#  Następny wczytaj listę haseł do programu, wylosuj jedno hasło z listy.
#  - wczytujemy linijkę 0 z pliku i dzielimy  przecinkiem,
#  -powstanie lista elementów -> wylosowac z niej 1 slowo i przedstawic
#   jak wisielca ---- + info o ilosci życ
#  -puytac o literkę
#  - jak zgadie to wstawic a jak nei odjąc zycie, jak wykozysta zycia to game over
#
#
#  Rozgrywka powinna być maksymalnie intuicyjna


fail_guess = 0


import random



def choose_category():
    categories = {
        1:"zwierzęta",
        2:'owoce',
        3:'warzywa'
    }
    print('Wybierz jedną z kategorii: ')
    for category_num, category_name in categories.items():
        print(f'{category_num}.kategoria {category_name}')

    while True:
        choice = int(input('Podaj nr kategorii--> '))
        if choice in categories:
            return categories[choice]
        else:
            print('Podaj poprawny numer kategorii--> ')





def choose_word(category):
    words = {
        'zwierzęta': ['kot', 'krowa', 'krokodyl','pies'],
        'owoce': ['jabłko', 'truskawka', 'borówka', 'ananas'],
        'warzywa': ['kalafior', 'burak', 'marchweka','seler' ]
    }

    return random.choice(words[category])




def display(word):
    word_guess = ["_"] * len(word)
    print(word_guess)
    return(word_guess)

def spr(word, word_guess, word_2):
    fail_guess = 0
    while fail_guess < 10:
        word1=""
        user_guess = str(input("Podaj litere: ")).lower()
        if user_guess in word:
            print("Bardzo dobrze!")
            pozytion = []
            for i in range(len(word)):
                if word[i] == user_guess:
                    pozytion.append(i)
            for i in pozytion:
                word_guess[i] = word[i]
            print(word_guess)
        else:
            print("Spróbuj jeszcze raz")
            fail_guess += 1
            print(word_guess)
            print(f"Nie ma {user_guess} w szukanym słowie. Pozostało Ci {10-fail_guess} prób")
        if word_2 == word_guess:
            print("Wspaniale odgadłeś haslo, ")
            print("".join(word_guess))
            break
        answer = str(input("Czy chcesz odgadnąć hasło [T/N]: ")).upper()
        if answer == "T":
            word1 = input('Podaj hasło: ').lower()
            if word1 == word_2:
                print("Wspaniale odgadłeś haslo, ")
                print("".join(word))
                break
            else:
                fail_guess += 1
                print(f"{word1} nie jest szukanym słowiem. Pozostało Ci {10 - fail_guess} prób")

                print(word_guess)



def main():
    category = choose_category()
    print("Gra wisielec bez wisielca")

    word = choose_word(category)
    print(f'hasło z kategorii {category} to: ')
    word_2 = word
    word_guess = display(word)
    spr(word, word_guess, word_2)



main()