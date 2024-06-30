# ##############################
# Bad Implementation (Liskov Substitution Principle)
# ##############################

# This is a bad implementation because Bird cannot be replaced with Penguin without affecting the correctness of the program

class Bird:
    def fly(self):
        print("I can fly")

class Penguin(Bird):
    def fly(self):
        print("I can't fly")
        
# Set Up
print("Bad Implementation (Liskov Substitution Principle)")
penguin = Penguin()

# Method Execution
penguin.fly()
print('\n')


# ##############################
# Good Implementation (Liskov Substitution Principle)
# ##############################

# This is a good implementation because subclasses of Bird can now be substituted without altering the correctness of the program
from abc import ABC, abstractmethod

class Bird(ABC):
    @abstractmethod
    def fly(self):
        pass

class FlyingBird(Bird):
    def fly(self):
        print("I can fly")

class NonFlyingBird(Bird):
    def fly(self):
        print("I can't fly")

class Penguin(NonFlyingBird):
    pass

# Set Up
print("Good Implementation (Liskov Substitution Principle)")
penguin = Penguin()

# Method Execution
penguin.fly()
