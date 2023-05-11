list_2d =[
    ["Dorota", "Wellman","dziennikarka"],
    ["Adam", "Małysz", "sportowiec"],
    ["Robert", "Lewandowski", "piłkarz"],
    ['Krystyna', "Janda", "aktorka"]
]
print(list_2d)
for row in list_2d:
    print()
    for id,elem in enumerate(row):
        if id ==1:
            print(elem, end=" - ")
        else:
            print(elem, end=" ")
    print()
    #print(row[0], row[1],'-' row[2])
    #print("-".join(row))
 

# print("------------------------------")
# for row in list_2d:
#     print(row)
#     for col in row:
#         print(col)
# arr = ["ala","ma", 'kota',"i", "psa"]
# for id in range(5):
#     if id == 2:
#         print(arr[id],end="****")
#     else:
#         print(arr[id], end="--->")
#     # print('hello', end="-")
#     # print('ma')
#     # print("lala",end='***')
print()
arr = ["ala","ma", 'kota',"i", "psa"]
print("----------->")
for id, word in enumerate(arr):
    print(id, word)