

trasa = float(input('Podaj liczbę kilometrów? '))
spalanie = float(input('Podaj spalanie? '))
cena = float(input('Podaj cenę paliwa? '))

d = trasa * spalanie/100
e = d * cena
print ("Zużyte paliwo", d)
print ("Cena paliwa", e)
