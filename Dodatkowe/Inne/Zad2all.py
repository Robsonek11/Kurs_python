# 2▹ Pobierz od użytkownika dowolny tekst i wyświetl tylko te znaki, które są na pozycjach parzystych.
# Wykonaj na dwa sposoby - za pomocą pętli oraz przez sting slicing ( ‘abrakadabra’ -> ‘baaar’).

txt = str(input('Podaj dowolny tekst '))
print(txt[1::2])
txt1=list(txt)

for id in txt1[1::2]:
    print (id, end="")




