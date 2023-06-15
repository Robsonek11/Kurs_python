from abc import ABC, abstractmethod


class Order(ABC):
    def __init__(self, items):
        self.items = items

    @abstractmethod
    def calculate_total(self) -> float:
        pass

    def display_order_summary(self):
        print("Order Summary:")
        for item in self.items:
            print(f"- {item}")
        print(f"Total: ${self.calculate_total()}")


class OnlineOrder(Order):
    def calculate_total(self) -> float:
        # Obliczanie całkowitej wartości zamówienia dla zamówienia online
        total = 0.0
        for item in self.items:
            total += item.price
        return total


class InStoreOrder(Order):
    def calculate_total(self) -> float:
        # Obliczanie całkowitej wartości zamówienia dla zamówienia w sklepie stacjonarnym
        total = 0.0
        for item in self.items:
            total += item.price * (1 - item.discount)
        return total


class Item:
    def __init__(self, name, price, discount=0.0):
        self.name = name
        self.price = price
        self.discount = discount


# Tworzenie zamówień
online_items = [
    Item("Product 1", 10.0),
    Item("Product 2", 20.0),
    Item("Product 3", 15.0)
]
online_order = OnlineOrder(online_items)

instore_items = [
    Item("Product 1", 10.0, 0.1),
    Item("Product 2", 20.0, 0.2),
    Item("Product 3", 15.0, 0.0)
]
instore_order = InStoreOrder(instore_items)

# Wyświetlanie podsumowania zamówień
online_order.display_order_summary()
print("\n")
instore_order.display_order_summary()