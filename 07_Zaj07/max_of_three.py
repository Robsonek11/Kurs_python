# maxofthree.py
def max_of_2(x, y):
  return x if x > y else y


def maximum_of(num1, num2, num3):
    return max_of_2(max_of_2(num1, num2), num3)

def main():

    v = maximum_of(a, b, c)
    print("Moja wieksza liczba to: ", v)
main()
