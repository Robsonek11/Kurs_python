#zad1
# korzystaj ze swojego kodu bmi.py. Rozbij liczenie bmi na funkcję obliczającą bmi na podstawie danych użytkownika oraz zwracającą
# odpowiednią wartość (niedowaga, waga normalna, nadwaga, otyłość) w zależności od otrzymanego parametru.
def get_numbers():
    num1 = input("Podaj wagę ->")
    num2= input("Podaj wzrost (w metrach) ->")

    w = float(num1.replace(",", "."))
    h = float(num2.replace(",", "."))

    return w, h



def bmi (num1, num2):
    bmi = num1 /(num2* num2)
    return bmi



def calculate_bmi (num1, num2):
    if bmi (num1, num2) < 15.99:
        print("Twoje BMI to \"wygłodzenie\":", round(bmi (num1, num2), 2))
    elif bmi (num1, num2)> 16 and bmi (num1, num2) < 16.99:
        print("Twoje BMI to \"wychudzenie\":", round(bmi (num1, num2), 2))
    elif bmi (num1, num2) > 17 and bmi (num1, num2) < 18.49:
        print("Twoje BMI to \"niedowaga\":", round(bmi (num1, num2), 2))
    elif bmi (num1, num2)> 18 and bmi (num1, num2) <24.99:
        print("Twoje BMI jest \"optymalne\":", round(bmi (num1, num2), 2))
    elif bmi (num1, num2) > 25 and bmi (num1, num2) < 29.99:
        print("Twoje BMI to \"nadwaga\":", round(bmi(num1, num2), 2))
    elif bmi (num1, num2) > 30 and bmi (num1, num2) < 34.99:
        print("Twoje BMI to \"otyłość I st\":", round(bmi(num1, num2), 2))
    elif bmi (num1, num2) > 35 and bmi (num1, num2) < 39.99:
        print("Twoje BMI jest \"otyłość II st\":", round(bmi(num1, num2), 2))
    else:
        print("Twoje BMI jest \"otyłość III st\":", round(bmi(num1, num2), 2))

def main():
    while True:
        num1, num2 = get_numbers()
        number = bmi(num1, num2)
        print(number)
        calculate_bmi(num1, num2)
        liczba = input(("chcesz policzyc jeszcze raz T/N"))
        if liczba.upper() == "N":
            break

main()
#zad2
#Nie korzystając z funkcji wbudowanej min(), napisz funkcję znajdującą maksymalną wartość z 3 liczb.maximum_of(a, b, c).
def min_of_two(val1, val2):
    return val1 if val1 < val2 else val2

    # if val1 > val2:
    #     return val1
    # else:
    #     return val2


def min_of_three(a, b, c):
    tmp = min_of_two(a, b)
    return min_of_two(c, tmp)

def main():
    # ---- glowny kod
    x, y, z = [15, 17
        , 2]
    result = min_of_three(x, y, z)
    print(result)

main()

#zad2a
import random
tab=[]
for i in range(3):
     number_los = random.randrange (1, 100)
     tab.append(number_los)
a,b,c = tab
print(tab)

def minimum_two(val1, val2):
    return val1 if val1 < val2 else val2

def minimum_number(tab):
    return  minimum_two(c, minimum_two(a,b))

result = minimum_number(tab)
print(result)

#zad3
# Nie korzystając z funkcji wbudowanej max(), napisz funkcję znajdującą maksymalną wartość z 3 liczb.maximum_of(a, b, c).
def max_of_two(val1, val2):
    return val1 if val1 > val2 else val2

    # if val1 > val2:
    #     return val1
    # else:
    #     return val2


def maximum_of(a, b, c):
    tmp = max_of_two(a, b)
    return max_of_two(c, tmp)

def main():
    # ---- glowny kod
    x, y, z = [15, 15, 2]
    result = maximum_of(x, y, z)
    print(result)

main()

#zad4
# Napisz  funkcję, która sprawdzi, czy liczba występuje w podanym przez użytkownika zakresie.Powinna zwrócić komunikat:
# “tak, liczba x znajduje się w zadanym zakresie”, “nie, liczba x jest z# poza  zakresu”

import random
def zakres():
    while True:
        item1 = int(input("Podaj początek zakresu ->"))
        item2= int(input("Podaj koniec zakresu ->"))
        if item1 > item2 or item2 -item1 >20:
            print('Podałeś zły zakres koniec musi być większy od początku lub długośc zakresu to 20' )
        else:
            break
    return item1, item2



def spr (num1, num2):
    liczba = random.randrange(1, 100)
    if liczba > num1 and liczba < num2:
        print(f"Tak, liczba {liczba} znajduje się w zadanym zakresie od {num1} do {num2}")
    else:
        print(f"Nie, liczba {liczba} nie znajduje się w zadanym zakresie od {num1} do {num2}")
    return


def main():
    while True:
        num1, num2 = zakres()
        spr(num1, num2)
        znak = input('chcesz spróbować jeszcze raz [T/N] -> ')
        if znak.upper() == "N":
            break

main()

#zad5
#Napisz grę ciepło - zimno tak, aby korzystać z funkcji

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