def czytaj_plik():
    with open('Pan_Tadeusz.txt') as fopen:
        content =fopen.read()
        return content

def wyswietlaj(content):
    print('******')
    print(content)
    print('******')

def main():
    fragment = czytaj_plik()
    wyswietlaj(fragment)

main()