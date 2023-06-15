class Produkt:
    def __init__(self, nazwa, cena):
        self.nazwa = nazwa
        self.cena = cena


class Sklep:
    def __init__(self):
        self.produkty = []

    def dodaj_produkt(self, produkt):
        self.produkty.append(produkt)

    def zobacz_produkt(self):
        if len(self.produkty) > 0:
            for produkt in self.produkty:
                print(f"Nazwa: {produkt.nazwa}, Cena: {produkt.cena}")
        else:
            print("Sklep nie posiada żadnych produktów.")

    def przymierz_produkt(self, nazwa_produktu):
        for produkt in self.produkty:
            if produkt.nazwa == nazwa_produktu:
                print(f"Możesz przymierzyć {produkt.nazwa}.")
                return
        print("Ten produkt nie jest dostępny w sklepie.")

    def kup_produkt(self, nazwa_produktu):
        for produkt in self.produkty:
            if produkt.nazwa == nazwa_produktu:
                print(f"Zakupiono produkt: {produkt.nazwa}.")
                self.produkty.remove(produkt)
                return
        print("Ten produkt nie jest dostępny w sklepie.")

    def zwroc_produkt(self, nazwa_produktu):
        for produkt in self.produkty:
            if produkt.nazwa == nazwa_produktu:
                print(f"Możesz zwrócić produkt: {produkt.nazwa}.")
                return
        print("Nie możesz zwrócić tego produktu.")


# Przykładowe użycie klasy Sklep
sklep = Sklep()
# Dodawanie produktów
koszula = Produkt("Koszula", 59.99)
spodnie = Produkt("Spodnie", 99.99)
buty = Produkt("Buty", 199.99)

sklep.dodaj_produkt(koszula)
sklep.dodaj_produkt(spodnie)
sklep.dodaj_produkt(buty)

# Wyświetlanie produktów
sklep.zobacz_produkt()

# Przymierzanie produktów
sklep.przymierz_produkt("Koszula")
sklep.przymierz_produkt("Spodnie")
sklep.przymierz_produkt("Buty")
sklep.przymierz_produkt("Kurtka")  # Produkt niedostępny

# Kupowanie produktów
sklep.kup_produkt("Spodnie")
sklep.kup_produkt("Buty")
sklep.kup_produkt("Koszula")  # Produkt niedostępny

# Zwrot produktów
sklep.zwroc_produkt("Spodnie")
sklep.zwroc_produkt("Kurtka")  # Zwrot niedostępny
