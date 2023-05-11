txt = input('Podaj tekst do zaszyfrowania: ')
number = int(input('Podaj wartość przesunięcia: '))
for i in txt:
    y = ord(i)

    x = y + number
    if y == 32:
        x = y
    if x > 90 and x < 97:
        a = x-90
        x = 97+a


    if x > 122 and x < 65:
        b = x - 122
        x = 65 + b


    # if x >= 97 and x <= 122:
    #     x = y + number
    #     #print(x)
    #
    # if x >= 65 and x <= 90:
    #     x = y + number
    #     print(x)


    z = chr(x)

    print(z, end='', sep=',')










    # if y > 65 or y < 90:
    #     if  x >= 90:
    #         w = number - 90
    #         z = chr(90+w)
    #         print(w)
    #     else:
    #         z = chr(y + number)
    #         print(w)
    # if y > 97 or y < 122:
    #     if x >= 122:
    #         w = number - 122
    #         z = chr(65 + w)
    #         print(w)
    #     else:
    #         z = chr(y + number)
    #         print(w)
    # print(z, end='', sep=',')


