# 1.	Napisz program, który wypisze liczby od 1 do 100, ale:
# o	jeśli liczba jest podzielna przez 3, zamiast niej wypisz "Fizz"
# o	jeśli liczba jest podzielna przez 5, zamiast niej wypisz "Buzz"
# o	jeśli liczba jest podzielna przez 3 i przez 5, zamiast niej wypisz "FizzBuzz"


for i in range(1,101):
    if i%2 ==0:
        print(f"Liczba {i} jest podzielna przez 2 ")
    if i%3 == 0:
        print(f"Liczba {i} jest podzielna przez 3 FIZZ")
    if i%5 ==0:
        print(f"Liczba {i} jest podzielna przez 5 BUZZ")
    if i%3 == 0 and i%5 == 0:
        print(f"Liczba {i} jest podzielna przez 3 i 5 FIIZZBUZZ")

