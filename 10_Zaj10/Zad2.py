# Utwórz klasę dla storczyków.Storczyki z zasady mają różne kolory, pory kwitnienia, gatunki.Utwórz dowolne
# atrybuty i metody.Dodaj atrybut wspólny dla wszystkich storczyków - królestwo roślin.

class storczyk:
    atrybut = 'królestwo roślin'
    def __init__(self, color, pora_kwit, gatunki):
        self.color = color
        self.pora_kwit = pora_kwit
        self.gatunki = gatunki

    def hau(self, lodyga):
        return f'łodyga {self.color}!' * lodyga

storczyk1 = storczyk('czerwony', 'wiosna', 'Dendrobium')
storczyk2 = storczyk('dyzio', 'biszkoptowy', 'Falenopsis')

print(storczyk1.hau(2))
