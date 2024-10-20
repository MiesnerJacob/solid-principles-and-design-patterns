# Concrete Implementation of Renderer

import pygame
from renderer.renderer import Renderer
from renderer.renderer_style import RendererStyle


class ClassicRenderer(Renderer):
    def init_pygame(self):
        super().init_pygame()
        pygame.display.set_caption("Game of Life - Classic")

    def get_colors(self):
        return {
            'background': (255, 255, 255),
            'cell': (0, 0, 0),
            'grid': (128, 128, 128),
            'start': (0, 255, 0),
            'pause': (255, 0, 0),
            'restart': (0, 0, 255),
            'text': (0, 0, 0),
            'slider': (128, 128, 128),
            'slider_button': (0, 0, 0),
        }
