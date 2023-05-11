counter = int(input('ile ksiązek chcesz dodać'))
title = input( 'Podaj tytuł ksiązki ')
review = input ('Podaj opinię o ksiązce(1-10) ')
data= {}
for i in range(counter):
    title = input('Podaj tytuł ksiązki ')
    review = input('Podaj opinię o ksiązce(1-10) ')
    data [title]= review
print(data)