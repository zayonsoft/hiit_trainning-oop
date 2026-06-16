class Car:
    speed = 0
    change_value = 10
    max_speed = 250
    engine_running = False

    def __init__(self, name, color) -> None:
        self.name = name
        self.color = color

    def start(
        self,
    ):
        self.engine_running = True

    def accelerate(self):
        if self.engine_running:
            self.speed += self.change_value

    def decelerate(self):
        if (self.speed - self.change_value) > 0:
            self.speed -= self.change_value
        else:
            self.speed = 0


class Vehicle:
    running = False

    def __init__(self, owner) -> None:
        self.owner = owner

    def is_running(self):
        if self.running:
            print(f"{self.owner}'s vehicle car is running")

        else:
            print(f"{self.owner}'s vehicle car is not running")


# the __init__ method
class Triangle:
    def __init__(self, a,b,c) -> None:
        self.a = a
        self.b = b
        self.c = c

