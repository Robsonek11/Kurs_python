
import random
def generate_test_instance(length, characters):
    sequence = [random.choice(characters)]
    while len(sequence) < length:
        if random.random() < 0.5:
            sequence.append(sequence[-1])
        else:
            sequence.append(random.choice(characters))
    return ''.join(sequence)

characters = input("Podaj znaki, oddzielając je przecinkami: ").split(',')
test_instance = generate_test_instance(4, characters)
print('teraz z podanych znaków stworzę ciąg:')
print(test_instance)