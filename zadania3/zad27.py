class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self, percent):
        self.price *= (1 - percent / 100)

produkt = Product("Laptop", 1000)
produkt.apply_discount(10)
print(produkt.price)