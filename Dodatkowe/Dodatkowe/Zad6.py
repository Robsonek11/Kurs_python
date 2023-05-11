# 6.	Napisz program do odwrócenia ciągu znaków podanego przez użytkownika (np. "hello" powinno być wyświetlone jako "olleh").
# a.	Za pomocą string slicing
# b.	Za pomocą pętli for
# c.	Za pomocą pętli while

txt = str(input('Podaj text '))
x = int(len(txt))
print(x)

print(txt[::-1])


for i in range(1,x+1):
     print(txt[-i])

print('--------------------------------------')
x = int(len(txt))-1
i = 0
while x >= 0:
    print(txt[x])
    x = x - 1
