# Thread Safe Singleton - Simple

import threading

class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if not cls._instance:
                cls._instance = super().__new__(cls)
        return cls._instance
    

if __name__ == "__main__":
    print("Creating instance of Singelton class!")
    singleton_1 = ThreadSafeSingleton()
    singleton_2 = ThreadSafeSingleton()
    if singleton_1 is singleton_2:
        print("Singelton instance created!")