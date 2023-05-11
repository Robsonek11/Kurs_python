#9.	Napisz program, który używa pętli for do wyznaczenia liczby wystąpień litery "a"
# w podanym przez użytkownika ciągu znaków.

txt = str(input("podaj ciąg znaków"))
b = 0
for i in txt:
    print(i)
    if i == "a":
        b = b + 1
print(f"Litera a występuje {b} razy")