from abc import ABC, abstractmethod
from typing import List
class FileSystemComponent(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def display(self, indent: int = 0):
        """Display information about the component. Must be implemented by subclasses."""
        pass

    @abstractmethod
    def get_size(self) -> int:
        """Get the size of the component. Must be implemented by subclasses."""
        pass

class File(FileSystemComponent):
    def __init__(self, name: str, size: int):
        super().__init__(name)
        self.size = size

    def display(self, indent: int = 0):
        print("    " * indent + f"└── File: {self.name}, Size: {self.size} bytes")

    def get_size(self) -> int:
        return self.size

class Directory(FileSystemComponent):
    def __init__(self, name: str):
        super().__init__(name)
        self.children: List[FileSystemComponent] = []

    def add(self, component: FileSystemComponent):
        self.children.append(component)

    def remove(self, component: FileSystemComponent):
        self.children.remove(component)

    def display(self, indent: int = 0):
        if indent == 0:
            print(f"📁 {self.name}/")
        else:
            print("    " * (indent-1) + f"└── 📁 {self.name}/")
        for child in self.children:
            child.display(indent + 1)

    def get_size(self) -> int:
        return sum(child.get_size() for child in self.children)
    
    def list_files(self):
        files = []
        for child in self.children:
            if isinstance(child, File):
                files.append(child.name)
            elif isinstance(child, Directory):
                files.extend(child.list_files())
        return files
    

#Usage
file1 = File("file1.txt", 1200)
file2 = File("file2.txt", 1500)
file3 = File("file3.txt", 1000)

dir1 = Directory("dir1")
dir2 = Directory("dir2")

dir1.add(file1)
dir1.add(file2)
dir2.add(file3)
dir1.add(dir2)

print("Before Removal:")
dir1.display()

print(f"Total size of {dir1.name} before removal: {dir1.get_size()} bytes")

print("\n Listing all files in dir1:")
print(dir1.list_files())

dir1.remove(file2)
dir1.remove(dir2)

print("\n After removal:")
dir1.display()

print("\nListing all files in dir1:")
print(dir1.list_files())
