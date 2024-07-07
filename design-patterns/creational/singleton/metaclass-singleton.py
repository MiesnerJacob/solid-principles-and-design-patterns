# Metaclass Implementation of Singleton Design Pattern

# Lazy loading version
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
    
class Singelton(metaclass=SingletonMeta):
    def some_business_logic(self):
        pass


print("Creating instance of Singelton class via lazy loading!")
singleton_1 = Singelton()
singleton_2 = Singelton()
if singleton_1 is singleton_2:
    print("Singelton instance created!")
print("\n")


# Eager loading version 1
class SingletonMeta(type):
    _instances = {}

    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)
        cls._instances[cls] = super().__call__()

    def __call__(cls, *args, **kwargs):
        return cls._instances[cls]

class Singelton(metaclass=SingletonMeta):
    def some_business_logic(self):
        pass


print("Creating instance of Singelton class via eager loading version 1!")
singleton_1 = Singelton()
singleton_2 = Singelton()
if singleton_1 is singleton_2:
    print("Singelton instance created!")
print('\n')


# Eager loading version 2
class SingletonMeta(type):
    _instances = {}

    def __new__(cls, *args, **kwargs):
        new_class = super().__new__(cls, *args, **kwargs)
        cls._instances[new_class] = super(SingletonMeta, new_class).__call__()
        return new_class

    def __call__(cls, *args, **kwargs):
        return cls._instances[cls]

class Singelton(metaclass=SingletonMeta):
    def some_business_logic(self):
        pass


print("Creating instance of Singelton class via eager loading version 2!")
singleton_1 = Singelton()
singleton_2 = Singelton()
if singleton_1 is singleton_2:
    print("Singelton instance created!")