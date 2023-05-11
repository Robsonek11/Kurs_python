# 4.	Napisz program, który używa pętli for do zsumowania wszystkich liczb parzystych
# z zakresu od 1 do 100.
a=0
for i in range(1,101):
    if i % 2 == 0:
        i += i
        a = a + i
print(f'Suma wszystkich liczb parzystych wynosi {a/2}')