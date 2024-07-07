# Thread Safe Singleton

import threading

# Simple implementation
class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if not cls._instance:
                cls._instance = super().__new__(cls)
        return cls._instance
    

print("Creating instance of Singelton class!")
singleton_1 = ThreadSafeSingleton()
singleton_2 = ThreadSafeSingleton()
if singleton_1 is singleton_2:
    print("Singelton instance created!")


# Metaclass implementation
class ThreadSafeSingleton(type):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton(metaclass=ThreadSafeSingleton):
    pass


# Prove the implementation is thread safe
print("Creating instance of Singelton class!")
def get_singleton_instance():
    s = Singleton()
    print(s)

threads = []

for i in range(10):
    t = threading.Thread(target=get_singleton_instance)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()