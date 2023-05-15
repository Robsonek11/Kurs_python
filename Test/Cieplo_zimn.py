#Napisz grę ciepło - zimno tak, aby korzystać z funkcji
# main(): Funkcja główna programu
#
# play_game(): Funkcja odpowiadająca za jedną rozgrywkę. Możemy się więc spodziewać, że w funkcji main będzie pętla wywołująca play_game() tak długo jak długo użytkownik będzie chciał grać
#
#
#
# get_user_number() - Pobierze wartość od użytkownika i sprawdzi że na pewno jest numerem
#
# check_guess():  Funkcja sprawdzająca, czy podana przez użytkownika liczba jest "ciepłej 🔥" czy "zimniej 🥶" w stosunku do wygenerowanej liczby. Może wykorzystywać wartość bezwzględną różnicy między liczbami w celu określenia, czy liczba jest bliska czy daleka (poprzedniau wartość wartości bezwzględnej będzie musiała być gdzieś przechowywana poza funkcją check_guess()  np w play_game i będzie przekazywana)

import random
def  get_computer_number():
    computer_number = random.randrange(1,100)
    return computer_number
def get_user_number():
    user_number = int(input("""Podaj liczbę z zakresu 1 do 100 
    Twoja liczba------>   """))
    return user_number

def play_game(comp, user):

    if abs(comp - user) < 5:
        print("gorąco, gorąco")
    elif abs(comp - user) < 10:
        print("cieplej cieplej")

    elif abs(comp - user) < 15:
        print("ciepło, ciepło")

    else:
        print('zimno')


def main():
    comp = get_computer_number()
    print(comp)
    while True:
        user = get_user_number()
        play_game(comp, user)
        if comp == user:
            print('Brawo odgadłes liczbę')
            end = input("""Czy chcesz zagrac? T/N
            Grasz->  """)
            if end.upper() == "N":
                break
            else:
                get_computer_number()
                comp = get_computer_number()
                print(comp)

main()


# print(get_computer_number())
# print((get_user_number()))


