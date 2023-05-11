# my_tuple = (3,6,45,89,2,14,11)
# num =int(input('podaj liczbe '))
#
# if num in my_tuple:
#     print('jest na krotce')
#     print(f'Numer{num} pod indeksem', my_tuple.index(num))
# else:
#     print('nie ma na krotce')

krotka = (1, 2, 3, 3, 2)
krot = set(krotka)
print(krot)


krotka1 = (1, 2, 3, 4, 5, 6)
krotka2 = (1, 2, 3, 5, 5, 6)

krotka_to_list = list(krotka1[:: 2] + krotka2[1:: 2])
print(krotka_to_list)

list_to_set = set(krotka_to_list)
print(list_to_set)