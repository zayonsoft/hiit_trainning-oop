# inheritance
class Animal:
    def __init__(self, name, no_of_legs) -> None:
        self.name = name
        self.no_of_legs = no_of_legs


class Dog(Animal):
    pass


my_dog = Dog(name="Frisky", no_of_legs=4)
