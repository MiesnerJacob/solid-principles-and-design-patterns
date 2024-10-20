import pygame
from renderer.renderer import Renderer
from renderer.renderer_style import RendererStyle

class DarkModeRenderer(Renderer):
    def init_pygame(self):
        super().init_pygame()
        pygame.display.set_caption("Game of Life - Dark Mode")

    def get_colors(self):
        return {
            'background': (30, 30, 30),  # Dark Gray
            'cell': (200, 200, 200),  # Light Gray
            'grid': (60, 60, 60),  # Medium Gray
            'start': (0, 200, 0),  # Dark Green
            'pause': (200, 0, 0),  # Dark Red
            'restart': (0, 0, 200),  # Dark Blue
            'text': (200, 200, 200),  # Light Gray
            'slider': (80, 80, 80),  # Medium Gray
            'slider_button': (150, 150, 150),  # Light Gray
        }
