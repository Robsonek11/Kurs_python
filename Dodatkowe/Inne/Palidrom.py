palidrom = str(input('Podaj swój wyraz zdanie'))
print(palidrom)
print(palidrom[::-1])

def czyPalindrom(x):
    x = x.lower().replace(" ", "") #zmieniamy wszystkie literki na male i pozbywamy sie spacji
    n = len(x) #zmienna pomocnicza przechowujaca dlugosc slowa
    for i in range(n-1):
        if x[i] != x[n-1-i]: #jezeli znak po przeciwnej stronie (w tej samej kolejnosci od konca) nie bedzie taki sam
            return False #zwroc false
    return True; #jezeli nie napotkano problemow, zwroc true
print("Program sprawdzajacy czy slowo jest palindromem")
print("Podaj slowo")
s1 = input() #pobieramy slowo
print("Podane slowo " + ("jest " if(czyPalindrom(s1)) else "nie jest ") + "palindromem")