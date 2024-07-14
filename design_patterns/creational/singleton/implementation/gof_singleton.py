# Gang of Four (GoF) Implementation of Singleton Design Pattern

class ClassicSingleton:
    _instance = None

    def __init__(self):
        raise RuntimeError("Call get_instance() instead.")
    
    @classmethod
    def get_instance(cls):
        # Note this is lazy instantiation of the class
        if not cls._instance:
            cls._instance = cls.__new__(cls)
        return cls._instance
    

if __name__ == "__main__":
    print("Creating instance of Singelton class!")
    singleton_1 = ClassicSingleton.get_instance()
    singleton_2 = ClassicSingleton.get_instance()
    if singleton_1 is singleton_2:
        print("Singelton instance created!")