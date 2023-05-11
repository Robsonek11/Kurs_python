password = str(input('Podaj hasło '))

length = len(password)
lower = password.islower()
digit = password.isalpha()
numeric = password.isalnum()
big = password.isupper()
#print ('Digit', digit)
#print('alafa nume',numeric)
if length < 8:
    print('Twoje hasło jest zakrótkie')
if lower == True:
    print('Twoje haslo nie ma duzej litery')
if big == True:
    print ('Nie ma małej litery')
if digit == True and numeric == True:
    print("Twoje hasło nie ma cyfry")
if numeric == True:
    print('Twoje hasło nie ma zanku alfanumerycznego')
else:
    print('Dobre hasło')