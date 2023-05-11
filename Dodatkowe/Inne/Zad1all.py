# Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem (np.jako jeden string rozdzielonych przecinkiem lub białym znakiem).
# Następnie powitaj każdą osobę na liście.


arr =str(input('Podaj listę słów po spacji '))
arr2 = arr.replace(" ", ",").split(',')
arr3 = list(arr2)
#arr2 = arr.split
print(arr3)
for i in arr3:
    print('Hello ', i)
