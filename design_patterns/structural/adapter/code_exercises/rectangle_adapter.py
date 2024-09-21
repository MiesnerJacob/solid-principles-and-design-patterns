from abc import ABC, abstractmethod

class Rectangle(ABC):
    @abstractmethod
    def __init__(self):
        pass

class LegacyRectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
class NewRectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

class RectangleAdapter(Rectangle):
    def __init__(self, new_rectangle: NewRectangle):
        self.x = new_rectangle.x1
        self.y = new_rectangle.y1
        self.width = new_rectangle.x2 - new_rectangle.x1
        self.height = new_rectangle.y2 - new_rectangle.y1

if __name__ == "__main__":
    new_rect = NewRectangle(10, 20, 50, 60)
    print("NewRectangle:")
    print(f"  Coordinates: ({new_rect.x1}, {new_rect.y1}) to ({new_rect.x2}, {new_rect.y2})")

    adapter = RectangleAdapter(new_rect)
    print("\nRectangleAdapter (converts NewRectangle to LegacyRectangle format):")
    print(f"  x: {adapter.x}, y: {adapter.y}, width: {adapter.width}, height: {adapter.height}")

    legacy_rect = LegacyRectangle(10, 20, 40, 40)
    print("\nEquivalent LegacyRectangle:")
    print(f"  x: {legacy_rect.x}, y: {legacy_rect.y}, width: {legacy_rect.width}, height: {legacy_rect.height}")

