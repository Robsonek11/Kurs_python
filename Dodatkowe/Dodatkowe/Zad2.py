#2. Napisz program, który używa pętli for do wyświetlenia tabliczki
#mnożenia (1 do 10) dla wybranej przez użytkownika liczby do.

number = int(input('Podaj liczbę od (1 do 10) -->'))
i = 1
b=0
for i in range(1, number):
    b=b+1
    i = i * number
    print(number,"*",b,"=",i)



