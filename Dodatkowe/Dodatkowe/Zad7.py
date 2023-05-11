# 7.	Napisz program, który używa pętli for do wyznaczenia największej liczby spośród:
# a.	[3, 6, 12, 54, 21, 35, 2, 9]
# b.	[9, 0, 30, 25, 44, 71, 42, 5, 17, 89, 39, 10, 22, 1]
# c.	Liczb w dowolnu sposób wprowadzonych przez użytkownika.


number = [3, 6, 12, 54, 21, 35, 2, 9]
x = max(number)
tab=[]
tab2=[]
tab3=[]
tab4=[]
dl = int(len(number))-1
print(x)
print(dl)
for i in range(dl):
    if number[i] <= number[i+1]:
        tab2.append(number[i])
        print(tab2)
    else:
        print(number[i])
        tab3.append(number[i])
        print(tab3)
dl1=len(tab3)-1
for i in range(dl1):
    if tab3[i] <= tab3[i+1]:
        tab3.append(tab3[i])
        print(tab3)
    else:
        print(tab3[i])
        tab4.append(tab3[i])
        print(tab4)

print(f" Najwieksza liczba w zbiorze {number} = {tab4}")


