def NWD(a, b):
    if b > 0:
        return (NWD(b,a%b))


    else:
        return a

print(NWD(186,18))