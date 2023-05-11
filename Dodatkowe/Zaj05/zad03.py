
a = int(input('podaj 1 liczbe: '))
b = int(input('podaj 2 liczbe: '))
c = int(input('podaj 3 liczbe: '))

if a > b or a > c:
    print('A jest najwieksza liczba')
if b > c:
    print('B jest najwieksza lista')
else:
    print('C jest najwieksza liczba i wynosi: ', c)
