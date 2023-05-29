"""Stwórz moduł, który przechowuje wzór na deltę.
Skorzystaj z wbudowanego modułu math.
W nowym pliku wykorzystaj moduł."""


import math

def delta(a, b, c):
    delta = math.sqrt(pow(b, 2)-4*a*c)
    return delta