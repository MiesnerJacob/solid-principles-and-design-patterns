# ##############################
# Bad Implementation (Interface Segregation Principle)
# ##############################

# This is a bad implementation because there are multiple methods in the interface that will not be used by all children

class IMultiFunctionDevice:
    def print(self):
        pass

    def scan(self):
        pass

    def copy(self):
        pass

    def fax(self):
        pass

class Printer(IMultiFunctionDevice):
    def print(self):
        print("Printing...")

class Scanner(IMultiFunctionDevice):
    def scan(self):
        print("Scanning...")

class Copier(IMultiFunctionDevice):
    def copy(self):
        print("Copying...")

class Fax(IMultiFunctionDevice):
    def fax(self):
        print("Faxing...")

class PrinterScanner(IMultiFunctionDevice):
    def print(self):
        print("Printing...")

    def scan(self):
        print("Scanning...")

# Set Up
print("Bad Implementation (Interface Segregation Principle)")
printer = Printer()
scanner = Scanner()
copier = Copier()
fax = Fax()
printer_scanner = PrinterScanner()

# Method Execution
printer.print()
scanner.scan()
copier.copy()
fax.fax()
printer_scanner.print()
printer_scanner.scan()
print("\n")


# ##############################
# Good Implementation (Interface Segregation Principle)
# ##############################

# This is a good implementation because the interfaces only contain methods used by the classes inheriting them
from abc import ABC, abstractmethod

class IPrinter(ABC):
    @abstractmethod
    def print(self):
        pass

class IScanner(ABC):
    @abstractmethod
    def scan(self):
        pass

class ICopier(ABC):
    @abstractmethod
    def copy(self):
        pass

class IFax(ABC):
    @abstractmethod
    def fax(self):
        pass

class Printer(IPrinter):
    def print(self):
        print("Printing...")

class Scanner(IScanner):
    def scan(self):
        print("Scanning...")

class Copier(ICopier):
    def copy(self):
        print("Copying...")

class Fax(IFax):
    def fax(self):
        print("Faxing...")

class PrinterScanner(IPrinter, IScanner):
    def print(self):
        print("Printing...")

    def scan(self):
        print("Scanning...")

# Set Up
print("Good Implementation (Interface Segregation Principle)")
printer = Printer()
scanner = Scanner()
copier = Copier()
fax = Fax()
printer_scanner = PrinterScanner()

# Method Execution
printer.print()
scanner.scan()
copier.copy()
fax.fax()
printer_scanner.print()
printer_scanner.scan()