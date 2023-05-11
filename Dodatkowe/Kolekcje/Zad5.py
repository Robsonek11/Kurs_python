# 5▹ Porównaj zachowanie discard() vs remove() dla typu set.

set1 = {1,2,3,4,5,6}
print (set1)
set1.discard(7)
print(set1)
set1.remove(7)
print(set1)

#remove zgłasza błąd gdy elementu nie ma