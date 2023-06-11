def email():
    lista = ['bb@op.pl', 'aa@op.pl', 'cc@op.pl']
    mail  = input('Podaj adres mailowy?')
    for i in lista:
        if i == mail:
            print(F'{i} ten mail jest na liście')
            return True
        else:
            return False

    print(' nie ma maila na liście')

def main():
    email()

main()