# # Utwórz listę lists_to_dict zawierającą listy 2 elementowe. Przekształć ją w słownik dict_from_list.
lists_to_dict = [["a", 1], ["b", 2], ["c", 3]]
#
dict_from_list=dict(lists_to_dict)
print(dict_from_list)

# Utwórz dowolną tablicę n x n zawierającą dowolny znak, a następnie wyświetl jej elementy w formie tabeli n x n. Elementy powinny być oddzielone spacją

number = int(input('Podaj liczbe '))
tab = [['-'] * number] * number
for row in tab:
    print(' ' .join(row))
