
with open('visa.txt', 'r') as visa, open('mastercard.txt', 'r') as mastercard, open('americanexpres.txt', 'r') as americanexpress:
    lines = visa and mastercard and americanexpress
    print(lines)
    for number in visa.readlines() and mastercard.readlines() and americanexpress.readlines():
        card_nr = number
        card_nr = card_nr.replace(" ", "")
        card_nr = card_nr.replace("-", "")
        print(card_nr)

