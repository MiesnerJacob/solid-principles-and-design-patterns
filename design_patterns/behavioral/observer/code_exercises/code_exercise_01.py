from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, product_name: str, new_stock: int) -> None:
        pass


class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self, product_name: str, new_stock: int) -> None:
        pass


class StoreManager(Observer):
    def __init__(self, name: str):
        self._name = name

    def update(self, product_name: str, new_stock: int) -> None:
        print(f"{self._name}: Stock level for {product_name} is now {new_stock}.")


class Inventory(Subject):
    def __init__(self, threshold: int = 10):
        self._observers = []
        self._products = {}
        self._threshold = threshold

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self, product_name: str, new_stock: int) -> None:
        for observer in self._observers:
            observer.update(product_name, new_stock)

    def update_stock(self, product_name: str, new_stock: int) -> None:
        self._products[product_name] = new_stock
        if new_stock < self._threshold:
            self.notify(product_name, new_stock)


if __name__ == "__main__":
    inventory = Inventory()
    
    # Adding products to inventory
    inventory._products = {
        "Apples": 10,
        "Oranges": 25,
        "Bananas": 50,
    }
    
    manager1 = StoreManager("Alice")
    manager2 = StoreManager("Bob")
    
    # Attaching store managers
    inventory.attach(manager1)
    inventory.attach(manager2)
    
    # Updating stock levels and checking notifications
    print("Stock level update 1:")
    inventory.update_stock("Apples", 5)
    print("\nStock level update 2:")
    inventory.update_stock("Bananas", 60)
    
    # Detaching manager1
    inventory.detach(manager1)
    
    # Updating stock levels again
    print("\nStock level update 3:")
    inventory.update_stock("Oranges", 20)
