# Stwórz program, który dla dowolnego ciągu znajduje najdłuższą sekwencję takich samych znaków oraz jej długość np.
# Wejście:
#var = ‘banannnnannnnnnnnnanananananaaaana’
# Wyjście
#‘nnnnnnnnn’, 9

import random
def sekwencja(word):
    max_sekwencja = ''
    aktualna_sekwencja = ''
    poprzednia_litera = None
    for litera in word:
        if litera == poprzednia_litera:
            aktualna_sekwencja = aktualna_sekwencja + litera

        else:

            if len(aktualna_sekwencja) > len(max_sekwencja):

                max_sekwencja = aktualna_sekwencja
            aktualna_sekwencja = litera
            poprzednia_litera = litera

    if len(aktualna_sekwencja) > len (max_sekwencja):

        max_sekwencja = aktualna_sekwencja


    return max_sekwencja, len(max_sekwencja)



def main():
    word =input('Podaj słowo ')
    wynik = sekwencja(word)
    print(f"Najdłuższa sekwencja w słowie {word} to ", wynik)
    print()
main()