from abc import ABC, abstractmethod
from enum import Enum, auto

# Old Bad code that we need to refactor
def calculate_shipping_cost(weight, carrier):
    cost = 0
    if carrier == "FedEx":
        cost = weight * 2.5
    elif carrier == "UPS":
        cost = weight * 3
    elif carrier == "DHL":
        cost = weight * 4
    return cost

print("Select a carrier for shipping:")
print("1. FedEx")
print("2. UPS")
print("3. DHL")

choice = int(input("Enter the number corresponding to your choice: "))
weight = float(input("Enter the weight of the package (in pounds): "))

if choice == 1:
    carrier = "FedEx"
elif choice == 2:
    carrier = "UPS"
elif choice == 3:
    carrier = "DHL"
else:
    print("Invalid choice!")
    exit(1)

shipping_cost = calculate_shipping_cost(weight, carrier)
print(f"The shipping cost for {carrier} is ${shipping_cost:.2f}")

# New Good Code that uses the Strategy Pattern
class ShippingCostCalculator(ABC):
    @abstractmethod
    def calculate_cost(self, weight: float) -> float:
        pass


class FedExShippingCostCalculator(ShippingCostCalculator):
    def calculate_cost(self, weight: float) -> float:
        return weight * 2.5


class UPSShippingCostCalculator(ShippingCostCalculator):
    def calculate_cost(self, weight: float) -> float:
        return weight * 3


class DHLShippingCostCalculator(ShippingCostCalculator):
    def calculate_cost(self, weight: float) -> float:
        return weight * 4
    
class AmazonShippingCostCalculator(ShippingCostCalculator):
    def calculate_cost(self, weight: float) -> float:
        return weight * 3.25


class Carrier(Enum):
    FedEx = auto()
    UPS = auto()
    DHL = auto()
    Amazon = auto()


class ShippingCostCalculatorFactory:
    @staticmethod
    def get_calculator(carrier_context: Carrier) -> ShippingCostCalculator:
        if carrier_context == Carrier.FedEx:
            return FedExShippingCostCalculator()
        elif carrier_context == Carrier.UPS:
            return UPSShippingCostCalculator()
        elif carrier_context == Carrier.DHL:
            return DHLShippingCostCalculator()
        elif carrier_context == Carrier.Amazon:
            return AmazonShippingCostCalculator()
        else:
            raise ValueError(f"Unsupported carrier: {carrier_context}")


class ShippingCostCalculatorContext:
    def __init__(self, carrier_context: Carrier):
        self.calculator = ShippingCostCalculatorFactory.get_calculator(carrier_context)

    def calculate_cost(self, weight: float) -> float:
        return self.calculator.calculate_cost(weight)


print("Select a carrier for shipping:")
print("1. FedEx")
print("2. UPS")
print("3. DHL")
print("4. Amazon")

choice = int(input("Enter the number corresponding to your choice: "))
weight = float(input("Enter the weight of the package (in pounds): "))

if choice == 1:
    carrier = Carrier.FedEx
elif choice == 2:
    carrier = Carrier.UPS
elif choice == 3:
    carrier = Carrier.DHL
elif choice == 4:
    carrier = Carrier.Amazon
else:
    print("Invalid choice!")
    exit(1)

shipping_cost = ShippingCostCalculatorContext(carrier).calculate_cost(weight)
print(f"The shipping cost for {carrier} is ${shipping_cost:.2f}")

