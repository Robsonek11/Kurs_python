w = input("Podaj wagę ->")
h = input("Podaj wzrost (w metrach) ->")

w = float(w.replace(",", "."))
h = float(h.replace(",", "."))

bmi = w / (h ** 2)
print (bmi)
if bmi < 15.99:
    print("Twoje BMI to \"wygłodzenie\":", round(bmi, 2))
elif bmi > 16 and bmi < 16.99:
    print("Twoje BMI to \"wychudzenie\":", round(bmi, 2))
elif bmi > 17 and bmi < 18.49:
    print("Twoje BMI to \"niedowaga\":", round(bmi, 2))
elif bmi > 18 and bmi <24.99:
    print("Twoje BMI jest \"optymalne\":", round(bmi, 2))
elif bmi > 25 and bmi < 29.99:
    print("Twoje BMI to \"nadwaga\":", round(bmi, 2))
elif bmi > 30 and bmi < 34.99:
    print("Twoje BMI to \"otyłość I st\":", round(bmi, 2))
elif bmi > 35 and bmi < 39.99:
    print("Twoje BMI jest \"otyłość II st\":", round(bmi, 2))
else:
    print("Twoje BMI jest \"otyłość III st\":", round(bmi, 2))