import random
print ("masz 6 prób")
i=0
x = random.randrange(1, 101)
while True:

    print('Zgadnij czy kolejna wylosowana liczba będzie wyższa czy niższa niż ',x,": \n")
    odp = str(input("-->"))

    if odp =="wyższa":
        i = i + 1
        y = random.randrange(1, 101)
        print("wylosowana liczba to ", y)
        if x < y:
            print(f"Gratulacje, wygrałeś! Kolejna liczba była wyższa niż {x}, Liczba prób: {i}")
            x = y
            break
        else:
            print(f"Niestety, przegrałeś. Kolejna liczba była niższa niż {x} Liczba prób: {i}")
            x = y

    if odp =="niższa":
        i = i + 1
        y = random.randrange(1, 101)
        print("wylosowana liczba to ", y)
        if x > y:
            print(f"Gratulacje, wygrałeś! Kolejna liczba była niższa niż {x}, Liczba prób: {i}")
            x = y
            break
        else:
            print(f"Niestety, przegrałeś. Kolejna liczba była wyższa niż {x} Liczba prób: {i}")
            x = y
    if i == 6:
        break