from shirt import Shirt
#first shirt is file Name another Shirt is class name

shirt_one = Shirt("Red", "L", "Long-sleeve", 25)
print(shirt_one.color)
print(shirt_one.size)
print(shirt_one.type)
print(shirt_one.price)
print("------------")

shirt_one.change_price(10)
print(shirt_one.price) 

shirt_one.color ='orange'
print(shirt_one.color)