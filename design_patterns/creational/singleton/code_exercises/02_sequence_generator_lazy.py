# Sequence Generator - Lazy Instantiation

class SequenceGenerator:
    _instance = None
    _count = 0

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    @classmethod
    def getNextNumber(cls):
        cls._count += 1
        print(cls._count)
    

print("Creating instance of Singelton class!")
sequence_generator_1 = SequenceGenerator()
sequence_generator_2 = SequenceGenerator()
sequence_generator_3 = SequenceGenerator()


print("Calling singleton to confirm correct implementation...")
sequence_generator_1.getNextNumber()
sequence_generator_2.getNextNumber()
sequence_generator_3.getNextNumber()