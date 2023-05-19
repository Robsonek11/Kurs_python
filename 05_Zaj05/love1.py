name1 = input("Podaj pierwsze imię: ")
name2 = input("Podaj drugie imię: ")


x = list(name1)
y = list(name2)

xy = list(x + y)


for i in xy:
    print(i)
    if i in x and i in y:
        x.remove(i)
        y.remove(i)

        print("kasujemy literkę")
    else:
        print("nie kasujemy literki")
print("".join(x), "".join(y))

if len(x) = len(y):
    print('Jesteście stworzeni dla siebie')
