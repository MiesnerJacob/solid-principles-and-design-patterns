# Metaclass Implementation of Singleton Design Pattern - Lazy Loading

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
    
class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        pass


print("Creating instance of Singelton class via lazy loading!")
singleton_1 = Singleton()
singleton_2 = Singleton()
if singleton_1 is singleton_2:
    print("Singelton instance created!")