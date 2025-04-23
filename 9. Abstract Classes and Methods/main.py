# 9. Abstract Classes and Methods
# Assignment:
# Use the abc module to create an abstract class Shape with an abstract method area().
# Inherit a class Rectangle that implements area().

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod  # @abstractmethod is a decorator => means this method must be implemented in subclasses
    def area(self):
        pass         # pass means "do nothing" or "not implemented yet"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = float(width)   # Convert to float or int
        self.height = float(height)
        
    def area(self):
        return self.width * self.height

# Example usage with input
width = input("Enter width: ")
height = input("Enter height: ")
rectangle = Rectangle(width, height)

print(f"Area of rectangle: {rectangle.area()}")
