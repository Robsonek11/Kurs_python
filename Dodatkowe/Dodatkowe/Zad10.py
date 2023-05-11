# 10.	Napisz program, który używa pętli while do zsumowania wszystkich liczb nieparzystych z
# zakresu od 1 do 100.
b = 1
i = 1
suma = 0
while i < 51:
    b = 2 * i - 1
    suma = suma + b
    i = i + 1
    print("ile liczb",b)
    print("suma", suma)
print(f'Suma wszystkich liczb parzystych wynosi {suma}')