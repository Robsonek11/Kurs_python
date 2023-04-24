#Zad2
s1 = 'Hello'
s2 = 'World'
s3 = s1[:3] + s2 + s1[3:5:1]
print(s3)
#Zad3
quote = '„Honesty is the first chapter in the book of wisdom."'
print(len(quote))
print(quote[45:51])
print(quote[45:])
lenght = int(len(quote)/2)
print(quote[:lenght])
print(quote[-2:-1])
print(quote[lenght::3])
print(quote[1:53:2])
print()
print(quote.replace('wisdom', 'friendship'))
#Zad4
book = str(input('Podaj tytuł ksiązki? '))
name = str(input('Nazwisko autora '))
pages =int(input('Liczba stron '))
print(book.title())
print(name.title())
print(pages)
txt = 'book'
" ".join("book")
print(" ".join(txt))
print(len(txt))
#Zad5
#Zad6
