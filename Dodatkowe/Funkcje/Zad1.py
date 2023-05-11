# Napisać funkcję, która oblicza pole koła na podstawie zadanego promienia.
pi=3.14
def field (num):
    pi = 3.14
    return pi*num**2

num = int(input("Podaj promien "))

print(f" Pole koła wynosi {field(num)}")