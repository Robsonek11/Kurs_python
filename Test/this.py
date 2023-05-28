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

def game(word):
    guessed_letters = []
    trials = 6
    hidden_word = "_ " * len(word)

    while trials > 0:
        print(f"\n{hidden_word}")
        print(f"Pozostało Ci : {trials} żyć.")
        letter = input("Podaj literę: ").lower()

        if letter in guessed_letters:
            print("Ta litera została już była.")
            continue

        guessed_letters.append(letter)

        if letter in word:
            new_hidden_word = ""
            for i in range(len(word)):
                if word[i] == letter:
                    new_hidden_word += letter
                else:
                    new_hidden_word += hidden_word[i]
            hidden_word = new_hidden_word

            if hidden_word == word:
                print("Brawo, zgadłeś!")
                break
        else:
            print("Zła litera.")
            trials -= 1

            if trials == 0:
                print("Przegrałeś! Hasło to:", word)
                break



def main():
    print("Gra wisielec bez wisielca")
    category = choose_category()
    word = choose_word(category)
    print(f'hasło z kategorii {category} to: ')
    game(word)



main()