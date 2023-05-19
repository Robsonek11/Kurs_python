txt = input('Podaj tekst do odszywrowania: ')
num = int(input('Podaj wartość przesunięcia: '))
szyfr=""
for i in range(len(txt)):

    if txt[i].isupper() and ord(txt[i]) - num < 65:
        szyfr = szyfr + chr(ord(txt[i]) - num + 26)

    elif txt[i].islower() and ord(txt[i]) - num < 97:
        szyfr = szyfr + chr(ord(txt[i]) - num + 26)
    elif txt[i] == " ":
        szyfr += " "
    else:
        szyfr = szyfr + chr(ord(txt[i]) - num)
print(szyfr)