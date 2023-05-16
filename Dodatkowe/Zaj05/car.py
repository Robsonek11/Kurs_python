# #zad8
# Napisz program, który będzie sprawdzał, czy nasz samochód kwalifikuje się do zarejestrowania jako zabytek.
#
#     Program zacznie ze stworzonym słownikiem o trzech kluczach:
#
#             marka (str)
#
#             model (str)
#
#             rocznik (int)
#
#     Wypisze ten słownik na ekran (bez żadnego formatowania)
#
#     Sprawdzi, czy samochód ma minimum 25 lat. Jeśli tak, wypisze komunikat:
#
#         “Gratulacje! Twój samochód (tutaj_marka) może być zarejestrowany jako zabytek.”
#
#     Jeśli nie spełnia powyższego warunku, wypisze komunikat:
#
#         “Twój samochód (tutaj_marka) jest jeszcze zbyt młody.”
#
#     Gdy program będzie poprawnie działał, pozmieniaj wartości słownika (ale nie klucze!), aby zobaczyć, czy progam również zmienia swoje zachowanie.
my_dict = {
    'marka':'',
    'model':'',
    'rocznik':'',
}
def dane():
    pd_marka = input('Podaj markę samochodu ')
    pd_model = input('Podaj markę samochodu ')
    pd_rocznik =input('Podaj rok produkcji samochodu ')
    my_dict['marka'] = pd_marka
    my_dict['model'] = pd_model
    my_dict['rocznik'] = pd_rocznik

def spr():
    if int(my_dict['rocznik']) <1998:
        print(f"Gratulacje! Twój samochód {my_dict['marka']} może być zarejestrowany jako zabytek.")
    else:
        print(f" Twój samochód {my_dict['marka']} jest jeszcze zbyt młody.")


def main():
    while True:
        dane()
        spr()
        num=input('chcesz sprawdzić jeszcze raz [T/N]')
        if num.upper() == 'N':
            break


main()


