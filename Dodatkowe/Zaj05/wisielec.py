# 10▹ Stwórz grę wisielec “bez wisielca”.
#
#     Komputer losuje wyraz z dostępnej w programie listy wyrazów.
#
#     Wyświetla zamaskowany wyraz z widoczną liczbą znaków (np. ‘- - - - - - -‘)
#
#     Użykownik podaje literę.
#
#     Sprawdź, czy litera istnieje w wyrazie. Jeśli tak, wyświetl mu komunikat:
#
#             “Trafione!” oraz napis ze znanymi literami.
#
#     W przeciwnym wpadku pokaż komunikat:
#
#             “Nie trafione, spróbuj jeszcze raz!”.
#
#     Możesz ograniczyć liczbę prób do np. 10.
import random
words_list = ['wakacje', 'plaża', 'telefon', 'komputer', 'telewizor', 'łazienka']

def word_los(words_list):
    my_words = random.choice(words_list)
    length = len(my_words)
    return (my_words)

def maskowanie():
    length = len(my_words)
    for i in range(length):
        print('-', end=" ")



# def guess_word(word):
#     answer_player = []
#     for i in word:
#         answer_player.append('*')




my_words = word_los(words_list)
length = len(my_words)
print(my_words)
print(length)
print(maskowanie())