# 6▹ Wywołaj błąd związany z otwarciem pliku.
#
#     Spróbuj odczytać plik, który nie istnieje.
#
#     Spróbuj odczytać wartość z pliku otwartym w trybie w
#
#     Spróbuj utworzyć plik, który już istnieje w trybie x
#
# Obsłuż w dowolny sposób każdy z powyższych błędów.

import random
def get_content():
    while True:
        try:
            filename = input('Podaj nazwe pliku (bez rozszerzenia txt)')
            with open(f'{filename}.txt') as fopen:
                content = fopen.readlines()
                return content
        except (FileNotFoundError, TypeError) as e:
            print("Nie ma takiego pliku", e)
            print("Spróbuj ponownie")


def get_content2():

        try:
            with open('save.txt', 'w' ) as fopen:
                massage = 'be or not to be'
                fopen.write(massage)
                # print(massage)
                # print(massage, file = fopen)
                print(massage, file = None)

        except (FileNotFoundError) as e:
            print("Nie ma takiego pliku", e)
            print("Spróbuj ponownie")
def get_write():
    while True:
        try:
            filename = input('Podaj nazwe pliku (bez rozszerzenia txt)')
            items = ['latarka', 'woda', 'namiot', "źdźbło", 'gąbka']
            with open(f'{filename}.txt', 'x', encoding='utf-8') as f:
                f.write('\n'.join(items))
                break
        except (FileExistsError) as e:
            print('pilk juz istnieje')







def show(quote):
    txt, author = quote.split(' - ')
    print('Quote of the day is:')
    print()
    width = 70
    print('*' * width)
    print(txt.center(width))
    print(author.strip().center(width))
    print('*' * width)


def main():
    # quotes = get_content()
    quotes2 = get_content2()
    # quote = random.choice(quotes)
    # show(quote)
    # file = get_write()


main()
