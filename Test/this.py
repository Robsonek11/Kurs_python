menu = {
    "Margherita": 15.00,
    "Capricciosa": 18.00,
    "Pepperoni": 20.00,
    "Quattro Formaggi": 22.00,
    "Vegetariana": 19.50
}

# Funkcja wyświetlająca menu
def display_menu():
    print("Menu:".center(20, "*"))
    for pizza, price in menu.items():
        print(f"{pizza} - cena: {price} zł")

# Funkcja przyjmująca zamówienie i sprawdzająca, czy wybrane przez klienta opcje menu są dostępne
def take_order():
    order = []
    while True:
        pizza = input("Jaką pizzę chcesz zamówić? (Wpisz 'koniec', aby zakończyć zamówienie): ")
        if pizza.lower() == "koniec":
            break
        elif pizza not in menu:
            print("Przykro nam, ta pizza nie jest dostępna.")
        else:
            order.append(pizza)
    return order

# Funkcja obliczająca łączny koszt zamówienia
def calculate_total(order):
    total = 0
    for pizza in order:
        total += menu[pizza]
    return total

# Wywołujemy funkcje, aby złożyć zamówienie
display_menu()
order = take_order()
total = calculate_total(order)
print(f"Twoje zamówienie to: {', '.join(order)}. Koszt: {total} zł.")
