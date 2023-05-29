def fib(num):
    sequence = []
    x, y = 0, 1

    while len(sequence) < num:
        sequence.append(x)
        x, y = y, x + y

    return sequence

def main():
    num = int(input('Podaj cyfrę dla ciągu fibonnaciego: '))
    sequence = fib(num)
    print(sequence)


main()