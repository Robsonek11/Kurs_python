import random
def get_content():
    filename = input('Podaj nazwe pliku (bez rozszerzenia txt)')
    with open(f'{filename}.txt') as fopen:
        content = fopen.readlines()

    return content

def main():
    quotes = get_content()

    print(quotes[0:5])
    for i in quotes[0:5]:
        print(i)
main()