# Sequence Generator - Eager Instantiation

class SequenceGeneratorMeta(type):
    _instances = {}
    _count = 0

    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)
        cls._instances[cls] = super().__call__()

    def __call__(cls, *args, **kwargs):
        return cls._instances[cls]

class SequenceGenerator(metaclass=SequenceGeneratorMeta):
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