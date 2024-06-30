# Open/Close Principle (OCP)

# Defintion: Software entities (classes, modules, functions, etc.) should be open for extension but closed for modification. This means that you should be able to add new functionality without changing existing code, typically achieved through abstraction and polymorphism.

# ##################
# Bad Implementation
# ##################

# This is bad implementation because the AreaCalculator class must be modified if we want to add new shapes!

import math

class AreaCalculator:
    def area(self, shape):
        if isinstance(shape, Circle):
            return math.pi * (shape.radius ** 2)
        if isinstance(shape, Rectangle):
            return shape.width * shape.height
        
class Circle:
    def __init__(self, radius):
        self.radius = radius

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

# Set Up
print("Bad Implementaton (Open/Close Principle)")
area_calculator = AreaCalculator()
circle = Circle(radius=1)
rectangle = Rectangle(width=3, height=1)

# Calculate areas for shapes
circle_area = area_calculator.area(circle)
print("Circle area:", circle_area)

rectangle_area = area_calculator.area(rectangle)
print("Rectangle area:", rectangle_area)
print('\n')


# ###################
# Good Implementation
# ###################

# This implementation is better because in order to create new shapes we just need to create a new shape class (extend), as opposed to modifying an existing object

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
class AreaCalculator:
    def area(self, shape):
        return shape.area()
        
# Set Up
print("Good Implementaton (Open/Close Principle)")
area_calculator = AreaCalculator()
circle = Circle(radius=1)
rectangle = Rectangle(width=3, height=1)

# Calculate areas for shapes
circle_area = area_calculator.area(circle)
print("Circle area:", circle_area)

rectangle_area = area_calculator.area(rectangle)
print("Rectangle area:", rectangle_area)