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
    waga  = float(input("Podaj wage w kilogramach: "))
    wzrost = float(input("Podaj wzrost w centymatrach: "))
    print("Twoje podpowiedzi: ", bmi.calculate_bmi(waga, wzrost))

main()