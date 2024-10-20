import pygame
from renderer.renderer import Renderer
from renderer.renderer_style import RendererStyle

class NeonRenderer(Renderer):
    def init_pygame(self):
        super().init_pygame()
        pygame.display.set_caption("Game of Life - Neon")

    def get_colors(self):
        return {
            'background': (0, 0, 0),  # Black
            'cell': (0, 255, 255),  # Cyan
            'grid': (0, 128, 128),  # Dark Cyan
            'start': (0, 255, 0),  # Neon Green
            'pause': (255, 0, 255),  # Neon Pink
            'restart': (255, 255, 0),  # Neon Yellow
            'text': (255, 255, 255),  # White
            'slider': (128, 0, 128),  # Purple
            'slider_button': (255, 0, 255),  # Neon Pink
        }
