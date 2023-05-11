#2▹ Utwórz listę L_test = [1, 2, 3, 4], krotkę T_test = (1, 2, 3, 4) oraz set S_test = {1, 2, 3, 4}. Jakie metody dostępne dla typu list nie będą działać dla typów tuple i set?
#zad2

L_test = [1 ,2, 3, 4]
T_test = (1, 2, 3, 4)
S_test = {1, 2, 3, 4}

L_test.append("5")
#T_test.append("5")
#S_test.append("5")
print(L_test)
print(T_test)
print(S_test)


L_test.append("5")
#T_test.append("5")
#S_test.append("5")
print(L_test)
print(T_test)
print(S_test)

L_test.extend(T_test)
print(L_test)
print(T_test)
print(S_test)


# Działa len(), max(), min(), sum(), any(), all(), sorted(), count(), index()
# Nie działa append(), clear(), copy(), extend(), index(), insert(), pop(), remove(), reverse(), sort()
