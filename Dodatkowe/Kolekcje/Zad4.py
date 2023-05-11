import random
tab=[]
number = int(input('Podaj liczbę losowanych liczb jako wielokrotność cyfry trzy '))
if number % 3 == 0:
    for i in range(number):
        x = random.randrange(1, 100)
        tab.append(x)
    print(tab)
    w = int(len(tab)/3)
    tab1 = tab[0:w]
    tab2 = tab[w:2*w]
    tab3 = tab[2*w:]

    print("Tablica 1",tab1)
    tab1.reverse()
    print("Tablica 1", tab1)
    
    print("Tablica 2",tab2)
    tab2.reverse()
    print("tablica 2", tab2)

    print("Tablica 3", tab3)
    tab3.reverse()
    print("tablica 3", tab3)
else:
    print('Nie podałeś wielokrotności liczby 3')