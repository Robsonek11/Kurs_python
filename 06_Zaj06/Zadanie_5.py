# Wykorzystaj plik zawierający fragment Pana Tadeusza.
# Znajdź najdłuższe słowo występujące w zadanym fragmencie.


def get_content():

    with open('Pan_Tadeusz.txt', encoding='UTF-8') as fopen:
        content = fopen.readlines()
    return content


def main():
    txt = get_content()

    print(txt)
    for i in txt:
        for j in txt:
            print(j)


main()