import random
tab=[]
for i in range(3):
     number_los = random.randrange (1, 100)
     tab.append(number_los)
a,b,c = tab
print(tab)

def minimum_two(val1, val2):
    return val1 if val1 < val2 else val2

def minimum_number(tab):
    return  minimum_two(c, minimum_two(a,b))

result = minimum_number(tab)
print(result)
