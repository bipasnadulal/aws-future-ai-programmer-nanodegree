class Clothing:
    def __init__(self, color, style, size, price):
        self.color = color
        self.style = style
        self.size = size
        self.price = price

    def change_price(self, price):
        self.price = price

    def calc_discount(self, discount):
        return self.price * (1-discount)

#shirt and pants classes have inherited from clothing class
class Shirt(Clothing):
    def __init__(self, color, style, size, price, long_or_shirt):
        Clothing.__init__(self, color, style, size, price) #inheriting all the attributes from parent class

        #initializing own attribute
        self.long_or_short = long_or_shirt

    def double_price(self):
        self.price = 2*self.price

class Pants(Clothing):
    def __init__(self, color, style, size, price, waist):
        Clothing.__init__(self, color, style, size, price)
        self.waist = waist

    def calc_discount(self, discount):
        return self.price * (1 - discount / 2)


