import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius

    def diameter(self):
        return 2 * self.radius

# Test your implementation
circle1 = Circle(3)
print(circle1.area())  # Should output approximately 28.274333882308138
print(circle1.circumference())  # Should output approximately 18.84955592153876
print(circle1.diameter())  # Should output 6

circle2 = Circle(5)
print(circle2.area())  # Should output approximately 78.53981633974483
print(circle2.circumference())  # Should output approximately 31.41592653589793
print(circle2.diameter())  # Should output 10
