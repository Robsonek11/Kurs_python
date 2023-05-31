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