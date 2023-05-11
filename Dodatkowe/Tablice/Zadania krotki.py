# Zadania
#
# 1▹ Stwórz krotkę zawierającą dane twojego pupila (rodzaj zwierzecia, rasa, jak się wabi). Następnie rozpakuj tę krotkę na pojedyńcze zmienne. Wykorzystaj zmienne do wyświetlenia f-stringa, tak by mogło powstać zdanie np. “Mój pies, rasy border collie wabi się Dyzio”.
#
# 2▹ Stwórz krotkę. Znajdź powtarzające się elementy krotki. Wyświetl je.
#
# 3▹ Stwórz krotkę liczb całkowitych. Poproś użytkownika o podanie dowolnej liczby. Jeśli liczba znajduje się na krotce wyswietl jej indeks.

#Zad1
pupil = ('kot', 'dachowiec', 'pusia')
(name, surname, year) = pupil

print(f"Moj {name} jest rasy {surname} wabi sie {year}")

#zad2

krotka = (1, 2, 3, 3, 2)


count = krotka.count(1)
if count >= 2:
    print('The count of 1 is:', count)

count = krotka.count(2)
if count >= 2:
    print('The count of 2 is:', count)
count = krotka.count(3)
if count >=2:
    print('The count of 3 is:', count)