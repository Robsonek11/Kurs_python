# Utwórz klasę dla storczyków.Storczyki z zasady mają różne kolory, pory kwitnienia, gatunki.Utwórz dowolne
# atrybuty i metody.Dodaj atrybut wspólny dla wszystkich storczyków - królestwo roślin.

class storczyk:
    atrybut = 'królestwo roślin'
    def __init__(self, kolor, pora_kwit, gatunki):
        self.kolor = kolor
        self.pora_kwit = pora_kwit
        self.gatunki = gatunki

    def opis(self):
        return f"Storczyk o kolorze {self.kolor}, kwitnie w {self.pora_kwit}, należy do gatunku {self.gatunki}."



    def zmiana_kolor(self, new_kolor):
        self.kolor = new_kolor

    def zmiana_kwit(self, new_pora_kwit):
        self.pora_kwit = new_pora_kwit

    def zmiana_gatunku(self, new_gatunki):
        self.gatunki = new_gatunki
storczyk1 = storczyk('czerwonym', 'wiosną', 'Dendrobium')
storczyk2 = storczyk('białym', 'biszkoptowy', 'Falenopsis')

print(storczyk1.opis())
print(storczyk2.opis())

storczyk1.zmiana_kolor('niebieski')
storczyk1.zmiana_kwit('zimą')
storczyk1.zmiana_gatunku('Phecostam')

print(storczyk1.opis())