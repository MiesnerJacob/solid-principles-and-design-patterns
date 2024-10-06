from abc import ABC, abstractmethod
import pygame
import time
from enum import Enum

class Color(Enum):
    RED = "Red"
    YELLOW = "Yellow"
    GREEN = "Green"
        
class TrafficLightState(ABC):
    @abstractmethod
    def next(self, light: 'TrafficLight') -> None:
        pass

    @abstractmethod
    def get_color(self) -> Color:
        pass


class GreenLight(TrafficLightState):
    def next(self, light: 'TrafficLight') -> None:
        light.current_state = RedLight()

    def get_color(self) -> Color:
        return Color.GREEN


class YellowLight(TrafficLightState):
    def next(self, light: 'TrafficLight') -> None:
        light.current_state = GreenLight()

    def get_color(self) -> Color:
        return Color.YELLOW


class RedLight(TrafficLightState):
    def next(self, light: 'TrafficLight') -> None:
        light.current_state = YellowLight()

    def get_color(self) -> Color:
        return Color.RED
    

class TrafficLight:
    def __init__(self):
        self.current_state = GreenLight()

    def next(self) -> None:
        self.current_state.next(self)

    def get_color(self) -> Color:
        return self.current_state.get_color()

# Define the simulation
class TrafficLightSimulation:
    def __init__(self):
        self.light = TrafficLight()
        self.cycle = 0
        self.screen = None
        self.width = 400
        self.height = 800

    def start(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Traffic Light Simulation')

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            self.cycle += 1
            self.light.next()

            self.draw()
            pygame.display.update()
            time.sleep(3)

    def stop(self) -> None:
        pygame.quit()

    def draw(self) -> None:
        # Fill the screen with light gray color
        self.screen.fill((211, 211, 211))

        red_color = (255, 0, 0)
        yellow_color = (255, 255, 0)
        green_color = (0, 255, 0)

        # Define the color of the traffic light outlines
        outline_color = (70, 70, 70)

        rect_x = self.width // 4
        rect_y = self.height // 8
        rect_width = self.width // 2
        rect_height = self.height // 1.5

        # Draw the rectangle for the traffic light fixture
        pygame.draw.rect(self.screen, outline_color, (rect_x, rect_y, rect_width, rect_height), 10)

        # Draw the outline and color of the red light
        radius = 50
        center_x = self.width // 2
        center_y = self.height // 2

        pygame.draw.circle(self.screen, outline_color, (center_x, center_y - (rect_height // 4)), radius + 5, 5)
        if self.light.get_color() == Color.RED:
            pygame.draw.circle(self.screen, red_color, (center_x, center_y - (rect_height // 4)), radius)
        else:
            pygame.draw.circle(self.screen, (211, 211, 211), (center_x, center_y - (rect_height // 4)), radius)

        # Draw the outline and color of the yellow light
        pygame.draw.circle(self.screen, outline_color, (center_x, center_y), radius + 5, 5)
        if self.light.get_color() == Color.YELLOW:
            pygame.draw.circle(self.screen, yellow_color, (center_x, center_y), radius)
        else:
            pygame.draw.circle(self.screen, (211, 211, 211), (center_x, center_y), radius)

        # Draw the outline and color of the green light
        pygame.draw.circle(self.screen, outline_color, (center_x, center_y + (rect_height // 4)), radius + 5, 5)
        if self.light.get_color() == Color.GREEN:
            pygame.draw.circle(self.screen, green_color, (center_x, center_y + (rect_height // 4)), radius)
        else:
            pygame.draw.circle(self.screen, (211, 211, 211), (center_x, center_y + (rect_height // 4)), radius)

if __name__ == '__main__':
    simulation = TrafficLightSimulation()
    
    try:
        simulation.start()
    except KeyboardInterrupt:
        simulation.stop()