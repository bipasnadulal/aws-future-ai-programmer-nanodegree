class Shirt:
    def __init__(self, color, size, type, price):
        self.color = color
        self.size = size
        self.type = type
        self.price = price

    def change_price(self, new_price):
        self.price = new_price


    def discount(self, discount):
        return self.price * (1 - discount)
