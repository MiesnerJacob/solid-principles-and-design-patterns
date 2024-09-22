from abc import ABC, abstractmethod
from enum import Enum, auto

# Bad Implementation not using strategy pattern
def process_text(text, operation):
    if operation == "uppercase":
        return text.upper()
    elif operation == "lowercase":
        return text.lower()
    elif operation == "capitalize":
        return text.capitalize()
    else:
        return text

input_text = "This is an example text."
operation = "uppercase"

output_text = process_text(input_text, operation)

# Good Implementation using strategy pattern

class TextProcessingStrategy(ABC):
    @abstractmethod
    def process(self, text):
        pass

class UppercaseStrategy(TextProcessingStrategy):
    def process(self, text):
        return text.upper()

class LowercaseStrategy(TextProcessingStrategy):
    def process(self, text):
        return text.lower()

class CapitalizeStrategy(TextProcessingStrategy):
    def process(self, text):
        return text.capitalize()

class TextProcessor:
    def __init__(self, strategy):
        self.strategy = strategy

    def process_text(self, text):
        return self.strategy.process(text)
    
class TextOperation(Enum):
    UPPERCASE = 1
    LOWERCASE = 2
    CAPITALIZE = 3

class TextProcessorFactory:
    @staticmethod
    def create_processor(operation):
        try:
            operation = TextOperation(int(operation))
            if operation == TextOperation.UPPERCASE:
                return TextProcessor(UppercaseStrategy())
            elif operation == TextOperation.LOWERCASE:
                return TextProcessor(LowercaseStrategy())
            elif operation == TextOperation.CAPITALIZE:
                return TextProcessor(CapitalizeStrategy())
        except ValueError:
            raise ValueError("Invalid operation")

if __name__ == "__main__":
    input_text = input("Enter a text: ")
    print("Select an operation:")
    print("1. UPPERCASE")
    print("2. LOWERCASE")
    print("3. CAPITALIZE")
    operation = input("Enter an operation number: ")

    processor = TextProcessorFactory.create_processor(operation)
    print(processor.process_text(input_text))