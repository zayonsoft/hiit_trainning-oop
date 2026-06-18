class Rectangle:
    color = "red"  # creating an attribute inside the class itself

    def __init__(self, length, breadth):
        self.length = length  # creating it inside a method
        self.breadth = breadth
        self.color = ""


obj1 = Rectangle(length=30, breadth=60)
