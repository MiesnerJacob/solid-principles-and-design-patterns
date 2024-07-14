# Sequence Generator - Thread Safe

import threading


class SequenceGeneratorMeta(type):
    _instances = {}
    _lock = threading.Lock()
    _count = 0

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super(SequenceGeneratorMeta, cls).__call__(*args, **kwargs)
            return cls._instances[cls]
        
class SequenceGenerator(metaclass=SequenceGeneratorMeta):
    @classmethod
    def getNextNumber(cls):
        with cls._lock:
            cls._count += 1
            print(cls._count)


print("Checking if implementation of thread safety and counter...")
def get_singleton_instance():
    SequenceGenerator().getNextNumber()

threads = []

for i in range(10):
    t = threading.Thread(target=get_singleton_instance)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()