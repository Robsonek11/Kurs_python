#Zad1
#Stwórz listę przedmiotów, które zabierzesz na samotną wyprawę w góry. Wyświetl nazwę właśnie spakowanego przedmiotu, po ostatnim #przedmiocie pokaż informację: “Great, we are ready!”

list = ['Latarka', 'Baterie', 'Telefon']

for i in list:
    print(i)
print('Great, we are ready!')

#zad2
#Utwórz listę, która zawiera składniki na ulubione danie. Wyświetl komunikaty co należy pokolei dodać. Poza pętlą umieść pozostałe #instrukcje np. “Wrzuć do pierkanika”, “Podawaj schłodzone”.
list = ['mleko', 'budyń', 'cukier', 'sok malinowy']
list2 = ['Podawaj schłodzone']
for i in list:
        print(i)
print(list2)

#zad3
#Napisz program, który dla 10 kolejnych liczb naturalnych wyświetli sumę poprzedników. Oczekiwany wynik: 1, 3, 6, 10, 15, 21, 28,
#36, 45, 55
k = int(input('Podaj liczbę '))
sum = 0
for i in range(1,k+1):
    sum = sum + i
    print(sum)

#zad4
#Napisz program, który wyświetli kolejne wyniki dla silni liczby naturalnej N (N podane przez użytkownika, ale nie większe niż 8).

k = int(input('Podaj liczbę '))
if k > 8:
    print('Podaj mniejsza liczbę')
else:
    silnia = 1
    for i in range(1,k+1):
        silnia = silnia * i
        print(silnia)