import bmi

def main():
    while True:
        num = input('czy chcesz jeszcze raz [T/N]')
        if num.upper() == 'T':

            waga = float(input("Podaj wage w kilogramach: "))
            wzrost = float(input("Podaj wzrost w centymatrach: "))
            wzrost
            print("Twoje podpowiedzi: ", bmi.calculate_bmi(waga, wzrost))
        else:
            print('koniec')
            break





main()