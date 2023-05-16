# 9▹ Kolejnym warunkiem, aby dostać “żółte tablice”, jest to, aby samochód posiadał co najmniej 75% oryginalnych części. W naszym zadaniu zakładamy, że rzeczoznawca określił jego oryginalność w kategorii tak/nie.
#
#     Poniżej stworzenia i wyświetlenia słownika w zadaniu powyżej:
#
#             dopisz do słownika nowy klucz czy_oryginalny i ustaw jego wartość (typ: bool) wedle uznania.
#
#             ponownie wyświetl zmieniony słownik
#
#     # Zmodyfikuj program tak, aby uwzględnił decyzję o możliwości zarejestrowania samochodu również od jego oryginalności. Dopisz odpowiednie komunikaty.



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
        else:
            my_dict['czy_orginalny'] =''
            print(my_dict)
            number = input('Czy twój samochód jest orginalny w 75%? [Yes/No]')
            if number.upper() == 'Y':
                my_dict['czy_orginalny'] = True
                print(f" Gratulacje! Twój samochód {my_dict['marka']} może być zarejestrowany jako zabytek.",
                my_dict)
            else:
                my_dict['czy_orginalny'] = False
                print(f"Twój samochód {my_dict['marka']} jest jeszcze zbyt młody", my_dict)



main()


