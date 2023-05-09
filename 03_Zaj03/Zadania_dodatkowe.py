# 1.	Napisz program, który pyta użytkownika o dwie liczby i wyświetla wynik ich mnożenia, ale tylko wtedy, gdy obie liczby są dodatnie. W przeciwnym wypadku wyświetl komunikat ”Nie mnożę!”

number1 = int(input('Podaj liczbę '))
number2 = int(input('Podaj liczbę '))

if number1 < 0 or number2 <0:
    print ('Nie mnoże')
else:
    wynik = number1 * number2
    print(f"Wynik mnożenia {wynik}")


#2. Napisz program, który używa pętli for do wyświetlenia tabliczki
#mnożenia (1 do 10) dla wybranej przez użytkownika liczby do.

number = int(input('Podaj liczbę od (1 do 10)'))
i=1
for i in range(number):
    i = i * number
    print(i)

# 3.	Napisz program, który wyświetla liczbę wyrazów w podanym przez użytkownika ciągu
# znaków (zakładamy, że wyrazy dzielą się spacją).

znak = str(input("Podaj ciąg znaków "))

print('Liczba wyrazów ',znak.split(' ') )
c = znak.count(" ")
print(f"Liczba wyrazów {c+1}")

# 4.	Napisz program, który używa pętli for do zsumowania wszystkich liczb parzystych
# z zakresu od 1 do 100.
a=0
for i in range(1,101):
    if i % 2 == 0:
        i += i
        a = a + i
print(f'Suma wszystkich liczb parzystych wynosi {a/2}')

# 5.	Napisz program, który używa pętli for do wyświetlenia gwiazdek w następującym kształcie. Liczba “pięter” powinna zależeć od liczby
# wprowadzonej przez użytkownika w zakresie od 4 do 10

number = int(input('Podja liczbę pięter '))
for i in range(number):
    txt="*"
    print(txt*i)

# 6.	Napisz program do odwrócenia ciągu znaków podanego przez użytkownika (np. "hello" powinno być wyświetlone jako "olleh").
# a.	Za pomocą string slicing
# b.	Za pomocą pętli for
# c.	Za pomocą pętli while

txt = str(input('Podaj text '))
x = len(txt)-1
print(x)

print(txt[::-1])


# for i in range(x, 0, -1):
#      print(txt[i])
#
#
# print('--------------------------------------')
# x=len(txt)-1
# i=0
# while i != x:
#     print(txt[i])
#     i = i - 1

# 7.	Napisz program, który używa pętli for do wyznaczenia największej liczby spośród:
# a.	[3, 6, 12, 54, 21, 35, 2, 9]
# b.	[9, 0, 30, 25, 44, 71, 42, 5, 17, 89, 39, 10, 22, 1]
# c.	Liczb w dowolnu sposób wprowadzonych przez użytkownika.


number = [3, 6, 12]
x=max(number)
tab=[]
tab2=[]
dl = int(len(number))-1
for i in range(dl):

    if number[i] > number[i+1]:
        tab2.append(number[i])
    else:
        temp=number[i]
        number[i]=number[i+1]
        number[i+1]= temp
        tab2.append(number[i])
print(tab2)

# 16.	Napisz program, który stworzy listę zawierającą 10 liczb losowych z zakresu od 1 do 100 (skorzystaj z modułu random) i
# wyświetla tylko te, które są mniejsze od 50.
import random
tab = []
tab2 = []
number = int(input('Podaj liczbę losowanych liczb '))
for i in range(number):
    x = random.randrange(1, 100)
    tab.append(x)
    if tab[i] < 50:
        tab2.append(i)
print(tab)
print(tab2)
