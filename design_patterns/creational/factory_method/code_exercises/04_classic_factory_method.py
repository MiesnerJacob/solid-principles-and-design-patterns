from abc import ABC, abstractmethod
from enum import Enum


class SpaceshipType(Enum):
    MILLENIUM_FALCON = "Millenium Falcon"
    UNSC_INFINITY = "UNSC Infinity"
    USS_ENTERPRISE = "USS Enterprise"
    SERENITY = "Serenity"


class Spaceship(ABC):
    def __init__(self, context):
        self.position = context["position"]
        self.size = context["size"]
        self.displayName = context["display_name"]
        self.speed = context["speed"]
    
    @abstractmethod
    def get_info(self) -> str:
        pass


class MilleniumFalcon(Spaceship):
    def get_info(self) -> str:
        return f"Ship Name: {self.displayName}, Ship Size: {self.size}, Ship Position: {self.position}, Ship Speed: {self.speed}"

class UNSCInfinity(Spaceship):
    def get_info(self) -> str:
        return f"Ship Name: {self.displayName}, Ship Size: {self.size}, Ship Position: {self.position}, Ship Speed: {self.speed}"

class USSEnterprise(Spaceship):
    def get_info(self) -> str:
        return f"Ship Name: {self.displayName}, Ship Size: {self.size}, Ship Position: {self.position}, Ship Speed: {self.speed}"

class Serenity(Spaceship):
    def get_info(self) -> str:
        return f"Ship Name: {self.displayName}, Ship Size: {self.size}, Ship Position: {self.position}, Ship Speed: {self.speed}"


class SpaceshipFactory(ABC):
    @abstractmethod
    def create_spaceship(self, context: dict) -> Spaceship:
        pass

class MilleniumFalconFactory(SpaceshipFactory):
    def create_spaceship(self, context: dict) -> Spaceship:
        return MilleniumFalcon(context)

class UNSCInfinityFactory(SpaceshipFactory):
    def create_spaceship(self, context: dict) -> Spaceship:
        return UNSCInfinity(context)

class USSEnterpriseFactory(SpaceshipFactory):
    def create_spaceship(self, context: dict) -> Spaceship:
        return USSEnterprise(context)

class SerenityFactory(SpaceshipFactory):
    def create_spaceship(self, context: dict) -> Spaceship:
        return Serenity(context)

def main():
    falcon_context = {"position": [0, 2], "size": [3, 2], "display_name": "Millenium Falcon", "speed": "Fast"}
    falcon_factory = MilleniumFalconFactory()
    falcon = falcon_factory.create_spaceship(falcon_context)
    print(falcon.get_info())

    infinity_context = {"position": [5, 3], "size": [4, 5], "display_name": "UNSC Infinity", "speed": "Very Fast"}
    infinity_factory = UNSCInfinityFactory()
    infinity = infinity_factory.create_spaceship(infinity_context)
    print(infinity.get_info())

    enterprise_context = {"position": [8, 4], "size": [6, 3], "display_name": "USS Enterprise", "speed": "Warp Speed"}
    enterprise_factory = USSEnterpriseFactory()
    enterprise = enterprise_factory.create_spaceship(enterprise_context)
    print(enterprise.get_info())

    serenity_context = {"position": [2, 96], "size": [1, 2], "display_name": "Serenity", "speed": "Moderate"}
    serenity_factory = SerenityFactory()
    serenity = serenity_factory.create_spaceship(serenity_context)
    print(serenity.get_info())

if __name__ == "__main__":
    main()
