# 16.	Napisz program, który stworzy listę zawierającą 10 liczb losowych z zakresu od 1 do 100 (skorzystaj z modułu random) i
# wyświetla tylko te, które są mniejsze od 50.
import random
tab=[]
tab2=[]
number = int(input('Podaj liczbę losowanych liczb '))
for i in range(number):
    x = random.randrange(1, 100)
    tab.append(x)
    if tab[i] < 50:
        tab2.append(i)
print(tab)
print(tab2)
