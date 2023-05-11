# Napisać funkcję, która przyjmuje listę liczb i zwraca sumę wszystki elementów na liście.

def sum (arr):
    result = 0
    for i in arr:
        result = result + int(i)
    return result

arr=[]

num = int(input("ile elementów chcesz podać ->"))

for _ in range(num):
    item = input("Podaj element, który chcesz dorzucic do listy1 ->")
    arr.append(item)




print(f"Suma {arr} wynosi {sum(arr)}")