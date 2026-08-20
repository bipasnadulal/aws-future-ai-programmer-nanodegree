class Shirt_ :
    def __init__(self, color, size, price):
        self.__price = price

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        self.__price = new_price

shirt_one = Shirt_('yellow', 'M', 23)
print(shirt_one.get_price())
shirt_one.set_price(20)
print(shirt_one.get_price())