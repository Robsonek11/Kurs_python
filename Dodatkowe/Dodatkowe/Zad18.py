# 2.	Napisz skrypt orzeł 🦅 / reszka 🪙, w której “komputer rzuca monetą” - losuje wynik.
# Program powinien pytać użytkownika,
# czy chce rzucać monetą ponownie, a także podawać wynik każdego rzutu.

import random



while True:
    x = random.randrange(0, 2)
    print(x)
    if x == 0:
        c = 'reszka'
        print(f"Rzucam monetą i wypadła {c}")
    else:
        c = 'orzeł'
        print(f"Rzucam monetą i wypadł {c}")
    wyb = str(input(f"Chesz ponownie rzucić monetą t/n --> "))
    if wyb == "t":
        continue
    if wyb == "n":
        break
