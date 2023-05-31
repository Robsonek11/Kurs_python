# 1▹ Stwórz listę składającą się z kilku elementów różnego typu np. [13, ‘string’, 2.45] itp.
# W pętli spróbuj wykonać dzielenie 10 przez wartość z listy. Złap wyjątki jakie mogą się przy tej okazji wydarzyć.

import sys

def main():
    candidate = [13, "string", 2.45, 0, True, False, (1, 2)]

    for i in candidate:
        try:
            a =10 / i
            print(a)
        except (TypeError, ZeroDivisionError) as te:
            print(te)


if __name__ == "__main__":
    main()