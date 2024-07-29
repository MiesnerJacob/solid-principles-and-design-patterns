from abc import ABC, abstractmethod

class User:
    def __init__(self, firstName, lastName, emailAddress, age=None, phoneNumber=None, address=None):
        self._firstName = firstName
        self._lastName = lastName
        self._emailAddress = emailAddress
        self._age = age
        self._phoneNumber = phoneNumber
        self._address = address

    @property
    def firstName(self):
        return self._firstName

    @property
    def lastName(self):
        return self._lastName

    @property
    def emailAddress(self):
        return self._emailAddress

    @property
    def age(self):
        return self._age

    @property
    def phoneNumber(self):
        return self._phoneNumber

    @property
    def address(self):
        return self._address

class UserBuilder(ABC):
    @abstractmethod
    def set_firstName(self, firstName):
        pass

    @abstractmethod
    def set_lastName(self, lastName):
        pass

    @abstractmethod
    def set_emailAddress(self, emailAddress):
        pass

    @abstractmethod
    def set_age(self, age):
        pass

    @abstractmethod
    def set_phoneNumber(self, phoneNumber):
        pass

    @abstractmethod
    def set_address(self, address):
        pass

class CustomUserBuilder(UserBuilder):
    def __init__(self):
        self.user = User(firstName="", lastName="", emailAddress="")

    def set_firstName(self, firstName):
        self.user._firstName = firstName

    def set_lastName(self, lastName):
        self.user._lastName = lastName

    def set_emailAddress(self, emailAddress):
        self.user._emailAddress = emailAddress

    def set_age(self, age):
        self.user._age = age

    def set_phoneNumber(self, phoneNumber):
        self.user._phoneNumber = phoneNumber

    def set_address(self, address):
        self.user._address = address

class UserDirector:
    def __init__(self, builder):
        self.builder = builder

    def build_user(self, specs):
        self.builder.set_firstName(specs["firstName"])
        self.builder.set_lastName(specs["lastName"])
        self.builder.set_emailAddress(specs["emailAddress"])
        if "age" in specs:
            self.builder.set_age(specs["age"])
        if "phoneNumber" in specs:
            self.builder.set_phoneNumber(specs["phoneNumber"])
        if "address" in specs:
            self.builder.set_address(specs["address"])

# Helper function to test the user building process
def test_user_building(specs, expected_output):
    builder = CustomUserBuilder()
    director = UserDirector(builder)
    director.build_user(specs)
    user = builder.user
    assert user.__dict__ == expected_output, f"Expected {expected_output}, but got {user.__dict__}"

# Test cases
test_specs = {
    'firstName': 'John',
    'lastName': 'Doe',
    'emailAddress': 'john.doe@example.com',
    'age': 30,
    'phoneNumber': '123-456-7890',
    'address': '123 Main St'
}

expected_output = {
    '_firstName': 'John',
    '_lastName': 'Doe',
    '_emailAddress': 'john.doe@example.com',
    '_age': 30,
    '_phoneNumber': '123-456-7890',
    '_address': '123 Main St'
}

test_user_building(test_specs, expected_output)

print("All tests passed!")