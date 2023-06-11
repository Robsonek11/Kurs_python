def foo_bar(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FooBar")
        elif i % 3 == 0:
            print("Foo")
        elif i % 5 == 0:
            print("Bar")
        else:
            print(i)

foo_bar(23)