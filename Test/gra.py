import random
# słownik wygrany: przegrany
slownik ={
    'p' : 'k',
    'k' : 'n',
    'n' : 'p'
}
print(slownik)
poprawne_odpowiedzi =['p', 'k', 'n']
print(poprawne_odpowiedzi)

def los_komputer():
    los = random.choice(poprawne_odpowiedzi)
    return los

print(los_komputer())

def odpowiedz_uzytkowanika():
    while True:
        odp = input ("""Podaj 
        p -> papier
        k -> kamien
        n -> nozyce\n
        twoja odpowiedz --> """)
        if odp in poprawne_odpowiedzi:
            break

        else:
            print('Podaj poprawną odpoweidz')
    return odp
def wynik(komp, uzytk):
    if komp == uzytk:
        print('->Remis<-')
    elif komp in slownik[uzytk]:
        print('->Uzytkownik wygrał<-')
    else:
        print('->Komputer wygrał<-')
def main():
    while True:
        komp = los_komputer()
        uzytk = odpowiedz_uzytkowanika()
        wynik(komp, uzytk)
        wybor = input("""Spróbuj jeszcze raz T/N
        Twój wybór -> """)
        if wybor.upper() == 'N':
            break
main()