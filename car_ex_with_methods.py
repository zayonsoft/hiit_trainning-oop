# methods
# Methods are functions inside classes or behaviours that an object can have
class Car:

    def __init__(self, color, brand, max_speed, year):
        self.color = color
        self.brand = brand
        self.max_speed = max_speed
        self.year = year

    def print_properties(self):
        print(f"Color: {self.color}")
        print(f"Brand: {self.brand}")
        print(f"Maximum Speed: {self.max_speed}")
        print(f"year: {self.year}")


my_car1 = Car(color="Blue", brand="Toyota", max_speed="180km/hr", year="2027")
my_car2 = Car(color="Red", brand="Korope", max_speed="120km/hr", year="1997")
my_car1.print_properties()
my_car2.print_properties()
