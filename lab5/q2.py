# Create abstract base class "shape" that has abstract method "area". Inherit rectangle, triangle
# and square class from shape class and provide implementation of "area" method for each
# derived class. Finally print area of rectangle, triangle and square.

from abc import ABC, abstractmethod

# Abstract base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Triangle class
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Square class
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

# Rectangle class
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Example usage
rectangle = Rectangle(5, 10)
triangle = Triangle(4, 6)
square = Square(3)

print(f"Area of Rectangle: {rectangle.area()}")
print(f"Area of Triangle: {triangle.area()}")
print(f"Area of Square: {square.area()}")
