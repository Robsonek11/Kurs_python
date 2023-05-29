"""Rozpoznawanie kart. Utwórz plik zawierający numery
kart kredytowych. Sprawdź dla każdej kart jej typ.
Podziel kart do plików wg typów
np. visa.txt, mastercard.txt, americanexpress.txt."""



###################################################
def get_card_numbers():
    with open('visa.txt', 'r') as visa, open('mastercard.txt', 'r') as mastercard, open('americanexpres.txt','r') as americanexpres:

        lines = visa.readlines()

        for l in lines:
            print("Line : " + l)
        # for number in visa.readlines():
        #     card_nr = number
        #     card_nr = card_nr.replace(" ", "")
        #     card_nr = card_nr.replace("-", "")
        #     print(card_nr)
        # for number in mastercard.readlines():
        #     card_nr = number
        #     card_nr = card_nr.replace(" ", "")
        #     card_nr = card_nr.replace("-", "")
        #     print(card_nr)
        # for number in americanexpres.readlines():
        #     card_nr = number
        #     card_nr = card_nr.replace(" ", "")
        #     card_nr = card_nr.replace("-", "")
        #     print(card_nr)
        return l


def is_visa(card_num):
    """Function that checks visa numbers"""
    # return card_num[0] == '4' and (len(card_num) == 16 or len(card_num) == 13)
    if card_num[0] == '4' and (len(card_num) == 16 or len(card_num) == 13):
        return card_num
    else:
        return False

# #
# def is_mastercard(card_num):
#     """Function that checks mastercard numbers"""
#     start_condition = int(card_num[0:2]) in range(51, 56) or int(card_num[0:4]) in range(2221, 2721)
#
#     return len(card_num) == 16 and start_condition
#     # if len(card_num) == 16 and start_condition:
#     #     return True
#     # else:
#     #     return False
#
#
# def is_amex(card_num):
#     """Function that checks amex numbers"""
#     return len(card_num) == 15 and card_num[0:2] in ('34', '37')
#     # if len(card_num) == 15 and card_num[0:2] in ('34', '37'):
#     #     return True
#     # else:
#     #     return False


def main():
    for i in get_card_numbers():
        print(i)

    numbers = get_card_numbers()
    print('💳 :', numbers)

        # if is_visa(number):
        #     visa =+i
        #     print("This is Visa card number", visa)
        # elif is_mastercard(number):
        #     master=+number
        #     print("This is MasterCard card number", master)
        # elif is_amex(number):
        #     amex=+number
        #     print("This is AmericanExpress card number", amex)
        # else:
        #     now=+number
        #     print("Unknown card number", now)





main()










