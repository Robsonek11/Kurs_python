# Pomyśl co sprawia, że ssak jest ssakiem? Utwórz klasę ssaki. Stwórz kilka obiektów klasy ssaki np. wilk, koń, ssaki.

class ssak:
    def __init__(self, nazwa, konczyny, oczy, pije_mleko):
        self.nazwa = nazwa
        self.konczyny = konczyny
        self.oczy = oczy
        self.pije_mleko = pije_mleko
    def karmi_mlekiem(self):
        if self.pije_mleko:
            print(f'{self.nazwa} jest ssakiem ma {self.konczyny} konczyny i {self.oczy}.oczu i młode pije mleko')
        else:
            print(f'{self.nazwa} jest ssakiem ma {self.konczyny} konczyny i {self.oczy}.oczu')

ssak1 = ssak("Wilk", 4, 2, False)
ssak1.karmi_mlekiem()


"""Pomyśl co sprawia, że ssak jest ssakiem? Utwórz klasę
 ssaki.
Stwórz kilka obiektów klasy ssaki np. wilk, koń, ssaki."""




#
# class Mammal:
#     def __init__(self, species, children):
#         self.species = species
#         self.children = children
#         self.zyworodne = True
#
#
#     def if_zyworodny(self):
#         if self.zyworodne:
#             print(f'{self.species} jest ssakiem żyworodnym, a jego dziecko to: {self.children}.')
#         else:
#             print(f'{self.species} nie jest ssakiem żyworodnym.')
#
# mammal1 = Mammal('Kot', 'koteczek')
# mammal1.if_zyworodny()
#
#
# mammal2 = Mammal('Pies', 'szczeniak')
# mammal2.if_zyworodny()