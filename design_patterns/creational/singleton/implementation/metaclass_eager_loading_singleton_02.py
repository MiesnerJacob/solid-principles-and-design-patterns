# Metaclass Implementation of Singleton Design Pattern - Eager Loading Version 2

class SingletonMeta(type):
    _instances = {}

    def __new__(cls, *args, **kwargs):
        new_class = super().__new__(cls, *args, **kwargs)
        cls._instances[new_class] = super(SingletonMeta, new_class).__call__()
        return new_class

    def __call__(cls, *args, **kwargs):
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        pass


if __name__ == "__main__":
    print("Creating instance of Singelton class via eager loading version 2!")
    singleton_1 = Singleton()
    singleton_2 = Singleton()
    if singleton_1 is singleton_2:
        print("Singelton instance created!")