# Pomyśl co sprawia, że ssak jest ssakiem? Utwórz klasę ssaki. Stwórz kilka obiektów klasy ssaki np. wilk, koń, ssaki.

class ssak:
    def __init__(self, konczyny, oczy ):
        self.konczyny = konczyny
        self.oczy = oczy


wilk = ssak (4, 2)


print(wilk.konczyny)