def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        answer = read_from_file('niedowaga.txt')
    elif bmi < 25:
        answer = read_from_file('waga_normalna.txt')
    elif bmi < 30:
        answer = read_from_file('nadwaga.txt')
    else:
        answer = read_from_file('otyłosc.txt')
    return answer


def read_from_file(filename):
    with open(filename) as f:
        lines = f.read()
        return lines
import bmi


def main():
    while True:
        try:
            weight = int(input('Podaj swoją wagę [kg]: '))
            height = float(input('Podaj swoj wzrost [m]: '))

            if weight > 597 or height > 2.80:
                raise ValueError('Nieprawdopodobne wartości')
            break
        except:
            print('Wartość nieprawidłowa, spróbuj jeszcze raz')
        return weight, height
    print("Twoje podpowiedzi: ", bmi.calculate_bmi(weight, height))

main()


