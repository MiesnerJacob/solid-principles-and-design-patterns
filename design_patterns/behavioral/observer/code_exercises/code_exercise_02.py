from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, subject) -> None:
        pass

class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify_observers(self) -> None:
        pass

class WeatherData(Subject):
    def __init__(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.observers = []

    def attach(self, observer: Observer) -> None:
        self.observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self.observers.remove(observer)

    def set_measurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.notify_observers()

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)


class CurrentConditionsDisplay(Observer):
    def __init__(self):
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0

    def display(self):
        print(f"Current conditions: {self.temperature}F degrees and {self.humidity}% humidity")

    def update(self, subject):
        self.temperature = subject.temperature
        self.humidity = subject.humidity
        self.pressure = subject.pressure
        self.display()


class StatisticsDisplay(Observer):
    def __init__(self):
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0

    def display(self):
        print(f"Statistics: {self.temperature}F degrees and {self.humidity}% humidity")

    def update(self, subject):
        self.temperature = subject.temperature
        self.humidity = subject.humidity
        self.pressure = subject.pressure
        self.display()


class ForecastDisplay(Observer):
    def __init__(self):
        self.current_pressure = 29.92
        self.last_pressure = 0

    def display(self):
        print(f"Forecast: {self.current_pressure} bar")

    def update(self, subject):
        self.last_pressure = self.current_pressure
        self.current_pressure = subject.pressure
        self.display()


if __name__ == "__main__":
    weather_data = WeatherData(80, 65, 30.4)
    current_conditions_display = CurrentConditionsDisplay()
    statistics_display = StatisticsDisplay()
    forecast_display = ForecastDisplay()

    weather_data.attach(current_conditions_display)
    weather_data.attach(statistics_display)
    weather_data.attach(forecast_display)

    weather_data.set_measurements(82, 70, 29.2)
    weather_data.set_measurements(78, 90, 29.2)
    weather_data.set_measurements(62, 95, 29.2)
