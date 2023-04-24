#Zad2
spalanie = float(input('Podaj spalnaie Twojego samochodu? (w litrach na 100km) '))
cena = float(input('Podaj cenę paliwa? (w PLN) '))
dystans = float(input('Podaj dystans jaki przejechałeś? (w kilometrach) '))
a = 6.4
b = 5.04
c = 1.2*6.4
print('Twoje auto spaliło ', dystans/100*spalanie, '(litrów)')
print('Za paliwo zapłacisz ', dystans/100*spalanie*cena, '(PLN)')
