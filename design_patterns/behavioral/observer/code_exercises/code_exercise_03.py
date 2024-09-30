from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, message: str) -> None:
        pass


class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class Stock(Subject):
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price
        self.observers = []

    def attach(self, observer: Observer) -> None:
        self.observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self.observers.remove(observer)

    def set_price(self, price):
        self.price = price
        self.notify()

    def notify(self) -> None:
        for observer in self.observers:
            observer.update(self)


class PriceDisplay(Observer):
    def update(self, stock: Stock) -> None:
        print(f"Price for {stock.symbol}: {stock.price}")


class ChangeDisplay(Observer):
    def __init__(self):
        self.last_price = 0
    
    def update(self, stock: Stock) -> None:
        change = stock.price - self.last_price
        print(f"Change for {stock.symbol}: {change}")
        self.last_price = stock.price
    

if __name__ == "__main__":
    stock = Stock("AAPL", 100)
    price_display = PriceDisplay()
    change_display = ChangeDisplay()

    stock.attach(price_display)
    stock.attach(change_display)
    
    stock.set_price(101)
    stock.set_price(120)
    stock.set_price(113)