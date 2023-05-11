# 3.	Napisz program, który wyświetla liczbę wyrazów w podanym przez użytkownika ciągu
# znaków (zakładamy, że wyrazy dzielą się spacją).

znak = str(input("Podaj ciąg znaków "))

print('Liczba wyrazów ',znak.split(' ') )
c = znak.count(" ")
print(f"Liczba wyrazów {c+1}")
