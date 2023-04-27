#zad1
#Napisz program zmieniający skalę w stopniach Fahrenheita na naszą w Celcjuszach. Program powinen wykonać się w pętli od 0 do 200 #stopni Fahrenheit, co 20 stopni.

   # C = 5/9 * (F - 32) # wzór Celsjusz → Fahrenheit

#Napisz rozwiązanie zarówno z użyciem pętli while jak i for.
print('Petla while')
f = 200
while f > 0:
    c=5/9*(f-32)
    print('Temperatura w stopniach Fahernheit',f)
    print('Temperatura w stopniach Fahernheit',c)
    f=f-20

print('Petla for')

for i in range(20, 220, 20):
    c = 5 / 9 * (i - 32)
    print('Temperatura w stopniach Fahernheit', i)
    print('Temperatura w stopniach Fahernheit', c)
#Zad2
#Napisz prostą grę, w której użytkownik musi zgadnąć liczbę od 0 - 20 ukrytą w programie (np. secret_num = 5). Pytaj użytkownika o #podanie liczby tak długo, aż nie zgadnie.

number = int(input('Podaj liczbe '))
secret_num = 5


while number != secret_num:
    print('Jeszcze raz')
    number = int(input('Podaj liczbe '))
print('Dobrze')