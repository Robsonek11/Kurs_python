#txt = "Kobyła ma mały bok"
#txt2 =txt[::-1]
#txt = txt.replace(' ',"" ).upper()
#print(txt)
#print(txt[::-1])
#print()
txt = input("Podaj tekst")
txt = txt.replace(' ',"" ).upper()
print("Tekst jest palidrom? ", txt == txt[::-1])