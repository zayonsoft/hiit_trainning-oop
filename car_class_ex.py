class Car:

    def __init__(self, color, brand, max_speed):
        self.color = color
        self.brand = brand
        self.max_speed = max_speed


my_car1 = Car(color="Blue", brand="Toyota", max_speed="180km/hr")
my_car2 = Car(color="Purple", brand="Lexus", max_speed="200km/hr")

my_car3 = Car(color="Pink", brand="Toyota", max_speed="250km/hr")


print(my_car1.color)
print(my_car1.brand)
print(my_car1.max_speed)
print("----------------")
print(my_car2.color)
print(my_car2.brand)
print(my_car2.max_speed)
print("----------------")
print(my_car3.color)
print(my_car3.brand)
print(my_car3.max_speed)
