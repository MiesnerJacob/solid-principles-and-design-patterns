from abc import ABC, abstractmethod

class Computer:
    def __init__(self):
        self.processor = None
        self.memory = None
        self.storage = None
        self.graphics_card = None
        self.operating_system = None
        self.extras = None


class ComputerBuilder(ABC):
    @abstractmethod
    def add_processor(self, processor):
        pass

    @abstractmethod
    def add_memory(self, memory):
        pass

    @abstractmethod
    def add_storage(self, storage):
        pass

    @abstractmethod
    def add_graphics_card(self, graphics_card):
        pass

    @abstractmethod
    def add_operating_system(self, operating_system):
        pass

    @abstractmethod
    def add_extras(self, extras):
        pass


class CustomComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer()

    def add_processor(self, processor):
        self.computer.processor = processor

    def add_memory(self, memory):
        self.computer.memory = memory

    def add_storage(self, storage):
        self.computer.storage = storage

    def add_graphics_card(self, graphics_card):
        self.computer.graphics_card = graphics_card

    def add_operating_system(self, operating_system):
        self.computer.operating_system = operating_system

    def add_extras(self, extras):
        self.computer.extras = extras



class ComputerDirector:
    def __init__(self, builder):
        self.builder = builder

    def build_computer(self, specs):
        self.builder.add_processor(specs["processor"])
        self.builder.add_memory(specs["memory"])
        self.builder.add_storage(specs["storage"])
        self.builder.add_graphics_card(specs["graphics_card"])
        self.builder.add_operating_system(specs["operating_system"])
        self.builder.add_extras(specs["extras"])


# Helper function to test the computer building process
def test_computer_building(specs, expected_output):
    builder = CustomComputerBuilder()
    director = ComputerDirector(builder)
    director.build_computer(specs)
    computer = builder.computer
    assert computer.__dict__ == expected_output, f"Expected {expected_output}, but got {computer.__dict__}"

# Test cases
test_specs = {
    'processor': 'Intel Core i5',
    'memory': '8GB',
    'storage': '512GB SSD',
    'graphics_card': 'Integrated',
    'operating_system': 'Windows 11',
    'extras': ['Wi-Fi']
}

expected_output = {
    'processor': 'Intel Core i5',
    'memory': '8GB',
    'storage': '512GB SSD',
    'graphics_card': 'Integrated',
    'operating_system': 'Windows 11',
    'extras': ['Wi-Fi']
}

test_computer_building(test_specs, expected_output)

print("All tests passed!")