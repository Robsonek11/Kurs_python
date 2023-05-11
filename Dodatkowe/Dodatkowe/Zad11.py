# 11.	Napisz program, który używa pętli while do wyświetlenia kolejnych liczb parzystych,
# aż do momentu, gdy ich suma przekroczy wartość 100.

b = 1
i = 1
suma = 0
while suma < 100:
    b = 2 * i - 1
    suma = suma + b
    i = i + 1

print(f'Suma wszystkich liczb parzystych wynosi {suma} od 1 do{b}')