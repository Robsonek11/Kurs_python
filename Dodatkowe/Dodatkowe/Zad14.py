# 14.	Napisz program, który używa pętli while do wyznaczenia
# liczby wystąpień litery "e" w podanym przez użytkownika ciągu znaków.
txt = str(input("podaj ciąg znaków "))

b = 0
i = 0
c = 0
while i != len(txt):
    b = txt[i]
    if b =="e":
       c = c + 1
    i = i + 1
print(f"Litera e występuje {c} razy")