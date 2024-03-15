from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def get_area(self):
        ...


class Rectangle(Shape):

    def get_area(self):
        return self.height * self.width

    def __init__(self, width, height):
        self.width = width
        self.height = height


class Triangle(Shape):
    def get_area(self):
        return (self.height * self.side) / 2

    def __init__(self, side, height):
        self.side = side
        self.height = height


class AreaCalculator:

    def __init__(self, shapes):
        self.shapes = shapes

    @property
    def shapes(self):
        return self.__shapes

    @shapes.setter
    def shapes(self, value):
        if not isinstance(value, list):
            raise AssertionError("Must be a list")

        self.__shapes = value

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.get_area()

        return total


shapes = [Rectangle(1, 6), Triangle(2, 3)]
calculator = AreaCalculator(shapes)

print("The total area is: ", calculator.total_area)
