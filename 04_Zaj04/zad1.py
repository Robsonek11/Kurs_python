def calc_area(radius):
    pi=3.14
    area = pi * radius ** 2
    return area



r= float(input('Podaj promien kola ->'))
print(calc_area(r))