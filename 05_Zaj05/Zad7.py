def number():
    number_card = str(input("Podaj numer karty "))
    if number_card.isdigit() == True and len(number_card) >= 13:
        return number_card
    else:
        print('To nie jest numer')


print(number())

def visa (number):
    if number_card[0] == 4 and len(number_card) == 13 or len(number_card) == 16:
        return(number_card)


print(visa)