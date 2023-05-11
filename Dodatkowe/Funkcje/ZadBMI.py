


w = input("Podaj wagę ->")
h = input("Podaj wzrost (w metrach) ->")

w = float(w.replace(",", "."))
h = float(h.replace(",", "."))

def bmi(w, h):
    bmi = w / (h * h)
    return bmi

print(bmi(w, h))


if bmi(w,h) < 15.99:
    print("Twoje BMI to \"wygłodzenie\":", round(bmi(w,h), 2))
elif bmi(w,h)> 16 and bmi(w,h) < 16.99:
    print("Twoje BMI to \"wychudzenie\":", round(bmi(w,h), 2))
elif bmi(w,h) > 17 and bmi(w,h) < 18.49:
    print("Twoje BMI to \"niedowaga\":", round(bmi(w,h), 2))
elif bmi(w,h)> 18 and bmi(w,h) <24.99:
    print("Twoje BMI jest \"optymalne\":", round(bmi(w,h), 2))
elif bmi(w,h) > 25 and bmi(w,h) < 29.99:
    print("Twoje BMI to \"nadwaga\":", round(bmi(w,h), 2))
elif bmi(w,h) > 30 and bmi(w,h) < 34.99:
    print("Twoje BMI to \"otyłość I st\":", round(bmi(w,h), 2))
elif bmi(w,h) > 35 and bmi(w,h) < 39.99:
    print("Twoje BMI jest \"otyłość II st\":", round(bmi(w,h), 2))
else:
    print("Twoje BMI jest \"otyłość III st\":", round(bmi(w,h), 2))

