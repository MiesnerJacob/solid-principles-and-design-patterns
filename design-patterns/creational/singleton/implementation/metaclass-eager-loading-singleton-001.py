# Metaclass Implementation of Singleton Design Pattern - Eager Loading Version 1

class SingletonMeta(type):
    _instances = {}

    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)
        cls._instances[cls] = super().__call__()

    def __call__(cls, *args, **kwargs):
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        pass


print("Creating instance of Singelton class via eager loading version 1!")
singleton_1 = Singleton()
singleton_2 = Singleton()
if singleton_1 is singleton_2:
    print("Singelton instance created!")