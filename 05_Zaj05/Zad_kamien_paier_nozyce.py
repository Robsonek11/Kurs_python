# papier kamien nozyce
import random
# słownik wygrany: przegrany

WINNERS = {
    'k': ('n', 'j'),
    'n': ('p', 'j'),
    'p': ('k', 's'),
    'j': ('p', 's'),
    's': ('n', 'k')
}

CORRECT_VALUES = ['k', 'n', 'p']
CORRECT_VALUES1 = ['k', 'n', 'p', 'j', 's']







def get_comp_choice():
    return random.choice(CORRECT_VALUES)
def get_comp_choice1():
    return random.choice(CORRECT_VALUES1)


def get_user_choice1():
    while True:
        user_choice1 = input("""Podaj wartość:
                k - kamień
                n - nożyce
                p - papier
                j - jaszczuka
                s - Spock
        -> """)

        if user_choice1 in CORRECT_VALUES1:
            break #return user_choice
        else:
            print('Nieprawidłowa wartość')
            print("--- spróbuj jeszcze raz! ---")

    return user_choice1


def get_user_choice():
    while True:
        user_choice = input("""Podaj wartość:
                k - kamień
                n - nożyce
                p - papier
               
        -> """)

        if user_choice in CORRECT_VALUES:
            break #return user_choice
        else:
            print('Nieprawidłowa wartość')
            print("--- spróbuj jeszcze raz! ---")

    return user_choice

def show_result(comp, user):
    if comp == user:
        print('Remis')
    elif comp in WINNERS[user]:
        print('Wygrana użytkownika')
    else:
        print('Wygrywa komputer')


def main():
    while True:

        choice = int(input("""Welcome:
                   1 - Difficulty level
                   2 - Easy level
                   3 - Quit
                   ---> """))
        #
        if choice == 2:
            print('Łatwy poziom')
            comp = get_comp_choice()
            user = get_user_choice()
            print("-------WYBORY --------")
            print(f'komputer -> {comp} vs user -> {user}')
            show_result(comp, user)

        elif choice == 1:
            print('Trudny poziom')
            comp = get_comp_choice1()
            user = get_user_choice1()
            print("-------WYBORY --------")
            print(f'komputer -> {comp} vs user -> {user}')
            show_result(comp, user)


        elif choice == 3:
            print("*** Dzięki za grę! *** ")
            break
        else:
            print('wybrałeś złą cyfrę')


main()