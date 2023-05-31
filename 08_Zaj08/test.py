# while True:
#     x = input('Podaj liczbe ')
#     if x.isdigit():
#         x = int()
#         break
#     else:
#         print('To nie jest liczba')
#

try:
    x = 8 / 0
except ZeroDivisionError as error:
    print('Pamiętaj kolego nie dziel przez zero')
    x = None
    print(error)
print('print')