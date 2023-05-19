
import random

# Generowanie losowych liczb
random_numbers = [random.randint(10, 20) for _ in range(16)]
print(random_numbers)
# Wyświetlanie tylko liczb powtarzających się
repeated_numbers = set()
unique_numbers = set()

for num in random_numbers:
    if num in unique_numbers:
        repeated_numbers.add(num)
    else:
        unique_numbers.add(num)

print("Liczby powtarzające się na liście to:")

for num in repeated_numbers:
    print(num)