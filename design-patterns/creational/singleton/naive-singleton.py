# Naive Implementation of Singleton Design Pattern

class Singleton:
    _instance = None

    def __new__(cls):
        # Note this is lazy instantiation of the class
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    

print("Creating instance of Singelton class!")
singelton_1 = Singleton()
if singelton_1:
    print("Singelton instance created!")