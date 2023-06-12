# Utwórz klasę Pracownik.
#
#     Pracownik ma stanowisko, wynagrodzenie, imie, nazwisko, staz pracy.
#
#     Pracownik powinen miec roczne podwyżki wg. dowolnie wymyślonego sposobu liczenia. Pracownik powinen odprowadzać podatek o wysokoci zależnej od swoich zarobków oraz minimalną składkę zdrowotną.
#
#     Pracownik powinien mieć pole typu boolowskiego zawierające status studenta. Jeśli pracownik jest studentem jego składka zdrowotna wynosi 0%.
#
#     Wszyscy pracownicy mają wspólną nazwę firmy. Spółgłoski imienia i nazwiska wraz z nazwą firmy .com tworzą adres mailowy. Np.
#
#     Adam Kowalski Love Python Company
#
#     email -> smkwlsk@lovepythoncompany.com

class pracownik:

  firma = 'Love Python Company'

  def __init__(self, imie, nazwisko, stanowisko,  staz):
    self.imie = imie
    self.nazwisko = nazwisko
    self.stanowisko = stanowisko
    self.staz = staz

  def email(self):
      firma = 'Love Python Company'
      napis =self.imie+self.nazwisko
      samogloski = ('a', 'e', 'i', 'y', 'o', 'u')
      spol = ""
      samo = ""
      for znak in napis:
          if znak in samogloski:
              samo += znak
          else:
              spol += znak


      return f' email:-->{spol.lower()}@'+self.firma

  def status_student (self, student ):
        return  print(student, 'is', bool(student))

  def wyplata (self, kwota):
      if kwota > 12000:
          kwota = kwota*0.66
          return print(f' wypłata {kwota}')
      else:
          kwota = kwota * 0.87
          return print(f' wypłata {kwota}')

  def podwyzka (self, kwota):
      if kwota > 12000:
          kwota = kwota*0.06
          return print(f' podwyżka {kwota}')
      else:
          kwota = kwota * 0.09
          return print(f' podwyżka {kwota}')


pracownik1 = pracownik('Michał', 'Rozum', 'magazynier', 5)

print(pracownik1.email())
print(pracownik1.status_student(0))
print(pracownik1.wyplata(14000))
