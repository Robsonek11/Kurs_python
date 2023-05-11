def even(num):
    if num % 2 == 0:
        num = 'parzysta'
        return num
    if num % 2 !=0:
        num = 'nieparzysta'
        return num
num = int(input("Podaj liczbe "))

print(f" Twoja liczba jest {even(num)}")