# Utwórz plik zawierający listę ok. 20 cytatów. Każdy cytat powinen się znaleźć w nowej linii. Utwórz funkcję, która losuje i wyświetla w sposób ciekawy cytat na dziś.
# Np. można wyświetlić tak:
# import random
#
# with open('cytaty.txt', 'r', encoding='utf-8') as fopen:
#     for line in fopen:
#         print('Quote of the day is:')
#         print('********************')
#         cytat = fopen.readlines()
#         losowy_cytat = random.choice(cytat)
#         print(losowy_cytat.strip())
#         print('********************')
import random

def get_content():
    with open('quotes.txt') as fopen:
        content = fopen.readlines()

    return content


def show(quote):
    print('Quote of the day is:')
    print()
    width = 60
    print('*' * width)
    print(quote.strip().center(width))
    print('*' * width)


def main():
    quotes = get_content()
    quote = random.choice(quotes)
    show(quote)

main()