
def spr_numer():
    while True:
        karta = input('Podaj numer karty...')
        karta = karta.replace(" ","")
        karta = karta.replace("-", "")
        if karta.isdigit()==True:
            print('To moze byc karta')
            break

        else:
            print('To nie jest karta')
            print('--->próbuj jeszcze raz<---')
    return karta

def czy_visa(numer_karty):
    if numer_karty[0] == '4' and (len(numer_karty) == 16 or len(numer_karty) == 13):
        return True
    else:
        return False
def czy_master(numer_karty):
    if int(numer_karty[0:2]) in range(51, 56) or int(numer_karty [0:4]) in range(2221, 2721):
        return True
    else:
        return False

def czy_american(numer_karty):
    if numer_karty[0:2] == ['34',37] and len(numer_karty) == 15:
        return True
    else:
        return False
numer = spr_numer()
print('7wi45yqc.bmp :', numer)

if czy_visa(numer) == True:
    print('To jest karta Visa')
elif czy_master(numer) == True:
    print('To jest karta Master')
elif czy_american(numer) == True:
    print('To jest karta American')
else:
    print('Nie znam tej karty')

print('🙈 🙈 🙈 🙈 🙈 🙈 🙈 🙈 🙈 🙈 🙈 🙈 🙈 🙈 🙈 🙈 🙈 🙈')
# # spr_kart(number)
# spr_kart(5527356928767069)