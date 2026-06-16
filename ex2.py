# talking about methods


class Car:

    # used to initialize attributes used in the class
    def __init__(self, name, brand, no_of_tyres):
        self.name = name
        self.brand = brand
        self.no_of_tyres = no_of_tyres

    def accelerate(self):
        print(f"{self.name} Is Accelerating............")


ferrari = Car(name="Favour's Ferrari", brand="Mobile Car", no_of_tyres=4)
ferrari_2 = Car(name="Samuel's Ferrari", brand="Mobile Car", no_of_tyres=8)

print(ferrari.name)
print(ferrari_2.name)
