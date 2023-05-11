# 5.	Napisz program, który używa pętli for do wyświetlenia gwiazdek w następującym kształcie. Liczba “pięter” powinna zależeć od liczby
# wprowadzonej przez użytkownika w zakresie od 4 do 10

number = int(input('Podja liczbę pięter '))
for i in range(number):
    txt="*"
    print(txt*i)