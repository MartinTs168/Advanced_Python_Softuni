from abc import ABC, abstractmethod
from math import pi as PI


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def calculate_perimeter(self):
        return 2 * PI * self.__radius

    def __init__(self, r):
        self.__radius = r

    def calculate_area(self):
        return PI * self.__radius ** 2


class Rectangle(Shape):

    def calculate_area(self):
        return self.__width * self.__height

    def calculate_perimeter(self):
        return self.__width * 2 + self.__height * 2

    def __init__(self, width, height):
        self.__width = width
        self.__height = height


circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())
rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())

