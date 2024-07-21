from abc import ABC, abstractmethod
from enum import Enum

# Step 0: Create an enumeration for animal types
class AnimalType(Enum):
    DOG = "Dog"
    CAT = "Cat"
    FISH = "Fish"

# Step 1: Create an abstract Animal class
class Animal(ABC):
    def __init__(self, context: dict):
        self.name = context['name']
        self.age = context['age']
    
    @abstractmethod
    def get_info(self) -> str:
        pass

# Step 2: Create concrete animal classes
class Dog(Animal):
    def get_info(self) -> str:
        return f"Dog Name: {self.name}, Age: {self.age}"

class Cat(Animal):
    def get_info(self) -> str:
        return f"Cat Name: {self.name}, Age: {self.age}"

class Fish(Animal):
    def get_info(self) -> str:
        return f"Fish Name: {self.name}, Age: {self.age}"

# Step 3: Create an AnimalFactory class
class AnimalFactory:
    def create_animal(self, animal_type: AnimalType, context: dict) -> Animal:
        if animal_type == AnimalType.DOG:
            return Dog(context)
        elif animal_type == AnimalType.CAT:
            return Cat(context)
        elif animal_type == AnimalType.FISH:
            return Fish(context)
        else:
            raise ValueError("Invalid animal type.")

# Step 4: Test the AnimalFactory class
def main():
    animal_factory = AnimalFactory()

    # Test the AnimalFactory by creating different types of animals
    dog_context = {"name": "Coco", "age": 6}
    dog = animal_factory.create_animal(AnimalType.DOG, dog_context)
    print(dog.get_info())

    cat_context = {"name": "Whiskers", "age": 3}
    cat = animal_factory.create_animal(AnimalType.CAT, cat_context)
    print(cat.get_info())

    fish_context = {"name": "Goldie", "age": 1}
    fish = animal_factory.create_animal(AnimalType.FISH, fish_context)
    print(fish.get_info())

if __name__ == "__main__":
    main()