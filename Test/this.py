
samogloski = ('a', 'e', 'i', 'y', 'o', 'u')
spol = ""
samo = ""
slowo = input("podaj słowo: ")
for znak in slowo:
    if znak in samogloski:
        samo += znak
    else:
        spol += znak

print(spol)
print(samo)

