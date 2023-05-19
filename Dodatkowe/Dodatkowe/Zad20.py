txt = input('Podaj tekst do zaszyfrowania: ')
num = int(input('Podaj wartość przesunięcia: '))
szyfr=""
for i in range(len(txt)):

    if txt[i].isupper() and ord(txt[i])+num > 90:
        szyfr = szyfr + chr(ord(txt[i]) + num - 26)

    elif txt[i].islower() and ord(txt[i])+num > 122:
        szyfr = szyfr + chr(ord(txt[i]) + num - 26)
    elif txt[i] == " ":
        szyfr += " "
    else:
        szyfr = szyfr + chr(ord(txt[i]) + num)
print(szyfr)