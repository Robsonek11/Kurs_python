handler = open("Pan_Tadeusz.txt")
print(handler.readline())
handler.close()

print('-----------------')

with open("Pan_Tadeusz.txt",encoding='UTF-8') as fo:
    print(fo.readline())
    print(fo)