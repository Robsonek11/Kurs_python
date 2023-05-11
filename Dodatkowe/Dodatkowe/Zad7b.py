# 7.	Napisz program, który używa pętli for do wyznaczenia największej liczby spośród:
# a.	[3, 6, 12, 54, 21, 35, 2, 9]
# b.	[9, 0, 30, 25, 44, 71, 42, 5, 17, 89, 39, 10, 22, 1]
# c.	Liczb w dowolnu sposób wprowadzonych przez użytkownika.


number = [9, 0, 2134, 25, 44, 71, 42, 5, 17, 1025, 39, 10, 22, 1]
print(type(number))


najwieksza = 0
for i in number:
      if najwieksza < i:
        najwieksza = i


print("największa liczba to:", najwieksza)

