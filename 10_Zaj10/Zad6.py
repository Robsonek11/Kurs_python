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

  def __init__(self, imie, nazwisko, stanowisko,  staz, wyplata, student):
    self.imie = imie
    self.nazwisko = nazwisko
    self.stanowisko = stanowisko
    self.staz = staz
    self.wyplata = wyplata
    self.student = student

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

  def podwyzka(self, procent):

      if self.wyplata > 12000:
          self.wyplata = self.wyplata + self.wyplata * (procent/100)
          return print(f'wypłata po rocznej podwyżce wyniesie: {self.wyplata}')
      else:
          self.wyplata = self.wyplata + self.wyplata * (procent/100)
          return print(f'wypłata po rocznej podwyżce wyniesie: {self.wyplata}')

  def obl_podatku(self):
      if self.student:
          return 0
      elif self.wyplata > 12000:
          return self.wyplata * 0.33
      else:
          return self.wyplata *0.1

  def skladka_zdrowotna(self):
      if self.student:
          return 0
      else:
          return self.wyplata * 0.01





def main():
    pracownik1 = pracownik('Michał', 'Rozum', 'magazynier',4, 10000, True)
    pracownik1.podwyzka(5)
    print(pracownik1.email())
    podatek= pracownik1.obl_podatku()
    print(f'podatek wyniesie: {podatek}')
    skladka = pracownik1.skladka_zdrowotna()
    print(f'składka zdrowotna wyniesie: {skladka}')

if __name__ == '__main__':
    main()