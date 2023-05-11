k = int(input('Podaj liczbę '))
if k > 8:
    print('Podaj mniejsza liczbę')
else:
    silnia = 1
    for i in range(1,k+1):
        silnia = silnia * i
        print(silnia)