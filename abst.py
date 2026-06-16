from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Square(Shape):
    def __init__(self, l) -> None:
        self.l = l

    def area(self):
        return self.l * self.l
