# 12.	Napisz program, który używa pętli while do wyświetlenia kwadratów kolejnych
# liczb całkowitych, począwszy od 1, aż do momentu, gdy wartość największego
# wyświetlonego kwadratu przekroczy wartość 100.
zakres = int(input('Podaj zakres liczb '))
b = 1
i = 1
kwadrat = 0
while kwadrat <= zakres:
    b = i
    kwadrat = b * b
    i = i + 1
if kwadrat >= zakres:
    b = b - 1
    kwadrat = b *b
    print(f'Kwadrat {b} wynosi {kwadrat} ')
