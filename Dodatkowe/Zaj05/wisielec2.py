import random
lista_slow_do_odgadniecia = ['wakacje', 'plaża', 'telefon', 'komputer', 'telewizor', 'łazienka']

def wybierz_slowo(lista_slow):
    wylowowane_slowo = random.choice(lista_slow_do_odgadniecia)
    return (wylowowane_slowo)

def tablica_do_str(tablica):
    str1= ""
    for i in tablica:
        str1 += i + " "
    return str1
def sprawdz_input(input_g):
    if input_g == "":
        print('Podaj jedną literę')
    elif len(input_g)>1:
        print('podales za duzo liter')
def zgdanij_slowo(slowo):
    odpowiedz_gracza = []
    for i in slowo:
        odpowiedz_gracza.append('*')

    zycia =8
    while (zycia > 0):
        print("\n Masz jeszcze" +str(zycia) + "żyć aby zgadnąć tajemnicze słowo")
        print("Tajemnicze słowo: " + tablica_do_str(odpowiedz_gracza))
        input_g =input('Podaj jedną literę')
        input_g= input_g.upper()

    print(slowo)
    print(odpowiedz_gracza)


print(zgdanij_slowo((wybierz_slowo(lista_slow_do_odgadniecia))))