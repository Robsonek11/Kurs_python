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
print(quote.split())
print(" {} {} {} {} {} {} {} {} {} {} ".format('Honesty', 'is', 'the', 'first', 'chapter', 'in', 'the', 'book', 'of', 'wisdom.'))
print(" {9} {8} {7} {6} {5} {4} {3} {2} {1} {0}".format('Honesty', 'is', 'the', 'first', 'chapter', 'in', 'the', 'book', 'of', 'wisdom.'))

#print(wyświetl cąły tekst odwrotnie)
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
palidrom = str(input('Podaj swój wyraz zdanie'))
print(palidrom)
print(palidrom[::-1])

#Zad6
txt = "Beautiful is better than ugly.\n Explicit is better than implicit.Simple is better than complex.\n Complex is better than complicated. Flat is better than nested. \nSparse is better than dense. \nReadability counts. Special cases aren\'t special enough to break the rules.Although practicality beats purity. \nErrors should never pass silently. \nUnless explicitly silenced. In the face of ambiguity, refuse the temptation to guess.\nThere should be one-- and preferably only one --obvious way to do it.\nAlthough that way may not be obvious at first unless you're Dutch.\nNow is better than never. Although never is often better than *right* now. If the implementation is hard to explain, it\'s a bad idea.\nIf the implementation is easy to explain, it may be a good idea.Namespaces are one honking great idea -- let\"s do more of those!"
print(txt.count("better"))
print(txt.replace('*', ' '))
print(txt.count("explain"))
print(txt.replace('explain', 'understand', 1))
print(txt.replace(' ', '-'))
txt.replace(' ', '.', ))
