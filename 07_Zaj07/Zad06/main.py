# Stwórz program, który dla dowolnego ciągu znajduje najdłuższą sekwencję takich samych znaków oraz jej długość np.
# Wejście:
#var = ‘banannnnannnnnnnnnanananananaaaana’
# Wyjście
#‘nnnnnnnnn’, 9

import random
def sekwencja(word):
    max_sekwencja = ''
    aktualna_sekwencja = ''
    poprzedni_znak = None
    for znak in word:
        if znak == poprzedni_znak:
            aktualna_sekwencja = aktualna_sekwencja + znak

        else:

            if len(aktualna_sekwencja) > len(max_sekwencja):

                max_sekwencja = aktualna_sekwencja
            aktualna_sekwencja = znak
            poprzedni_znak = znak

    if len(aktualna_sekwencja) > len (max_sekwencja):

        max_sekwencja = aktualna_sekwencja


    return max_sekwencja, len(max_sekwencja)



def main():
    word =input('Podaj słowo ')
    wynik = sekwencja(word)
    print(f"Najdłuższa sekwencja w słowie {word} to ", wynik)
    print()
main()