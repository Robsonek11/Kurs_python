# 15.	Napisz program, który wyświetla sumę wszystkich liczb parzystych z zakresu od 1 do 100.
# Dodaj przy liczbie wykrzyknik tylko wtedy, gdy liczba jest podzielna przez 3.
b = 1
i = 0
c = 0
suma = 0
while i < 51:
    b = 2 * i
    suma = suma + b
    i = i + 1
    if suma % 3 == 0:
        c = "!"
    else:
        c = ""
    print(f"Suma {b} parzystych  liczb wynosi {suma} i {c}")

print(f'Suma wszystkich liczb parzystych wynosi {suma} {c} od 1 do {b}')