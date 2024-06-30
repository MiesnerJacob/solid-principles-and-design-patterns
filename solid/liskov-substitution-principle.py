# ##############################
# Bad Implementation (Liskov Substitution Principle)
# ##############################

# This is bad implementation because Bird cannot be replaced with penguin without affecting the correctness of the program

class Bird:
    def fly(self):
        print("I can fly")

class Penguin(Bird):
    def fly(self):
        print("I can't fly")
        
# Set Up
print("Bad Implementaton (Liskov Substitution Principle)")
penguin = Penguin()

# Method Execution
penguin.fly()
print('\n')


# ##############################
# Good Implementation (Liskov Substitution Principle)
# ##############################

# This is good implementation becauser subclasses of Bird can now be substituted without altering the correctness of the program

class Bird:
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
print("Good Implementaton (Liskov Substitution Principle)")
penguin = Penguin()

# Method Execution
penguin.fly()