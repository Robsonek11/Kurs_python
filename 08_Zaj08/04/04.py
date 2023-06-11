# Oblicz średnią arymetyczną z kilku liczb. Liczby będą podane przez użytkownika po przecinku. Napisz funkcję,
# która przyjmie wartości i wyświetli średnią. Program powinen być odporny na błędy użytkownika.
# Błędów nie wyświetlaj, ale rodzaj błędu zapisz do pliku.

from modul import srednia
def get_numbers():
    numbers = []
    num = None
    print("\nAby przerwać wprowadzanie liczb, podaj 0 (zero).")
    while not num:
        try:
            num = float(input("Podaj liczbe (1-100): "))
            if (num > 0 and num < 101):
                numbers.append(float(num))

            elif num == 0:
                break
            else:
                print("Błędna liczba.")
            num = None
        except ValueError as te:
            num =
            with open('bledy.txt', 'w') as f:
                # print(te)
                f.write('ValueError')


    return numbers

def main():
    s = srednia(get_numbers())
    print(s)



if __name__ == '__main__':
    main()