import pygame
from abc import ABC, abstractmethod
from renderer.renderer_style import RendererStyle

class Renderer(ABC):
    def __init__(self, width, height, cell_width, cell_height):
        self.width = width
        self.height = height
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.screen = None
        
        # Initialize Pygame first
        self.init_pygame()
        
        # Now it's safe to create fonts
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        
        # Button positions
        button_y = self.height - 60
        self.start_button = pygame.Rect(10, button_y, 100, 50)
        self.pause_button = pygame.Rect(120, button_y, 100, 50)
        self.restart_button = pygame.Rect(230, button_y, 100, 50)
        self.slider_rect = pygame.Rect(340, self.height - 55, 200, 40)
        self.slider_button_rect = pygame.Rect(340, self.height - 50, 20, 30)
        self.slider_min = 0.5  # Slowest speed (longest interval)
        self.slider_max = 0.05  # Fastest speed (shortest interval)

        # Adjust the Change Style button to be wider
        change_style_button_width = 200  # Increased from 150 to 200
        self.change_style_button = pygame.Rect(
            self.width - change_style_button_width - 10,  # 10 pixels from the right edge
            self.height - 55,
            change_style_button_width,
            40
        )
        self.style_options = list(RendererStyle)
        self.current_style = RendererStyle.CLASSIC

    def init_pygame(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Game of Life")

    @abstractmethod
    def get_colors(self):
        pass

    def render(self, grid, is_running):
        colors = self.get_colors()
        self.screen.fill(colors['background'])
        self.draw_grid(colors)
        self.draw_cells(grid, colors)
        self.draw_buttons(is_running, colors)
        pygame.display.flip()

    def draw_grid(self, colors):
        grid_height = self.height - 70  # Leave space for buttons
        for y in range(0, grid_height, self.cell_height):
            for x in range(0, self.width, self.cell_width):
                cell = pygame.Rect(x, y, self.cell_width, self.cell_height)
                pygame.draw.rect(self.screen, colors['grid'], cell, 1)

    def draw_cells(self, grid, colors):
        for y in range(len(grid.cells)):
            for x in range(len(grid.cells[0])):
                cell = pygame.Rect(x * self.cell_width, y * self.cell_height, self.cell_width, self.cell_height)
                if grid.cells[y][x].is_alive():
                    pygame.draw.rect(self.screen, colors['cell'], cell)

    def draw_buttons(self, is_running, colors):
        # Draw Start button
        pygame.draw.rect(self.screen, colors['start'], self.start_button)
        start_text = self.font.render("Start", True, colors['text'])
        start_text_rect = start_text.get_rect(center=self.start_button.center)
        self.screen.blit(start_text, start_text_rect)

        # Draw Pause button
        pygame.draw.rect(self.screen, colors['pause'], self.pause_button)
        pause_text = self.font.render("Pause", True, colors['text'])
        pause_text_rect = pause_text.get_rect(center=self.pause_button.center)
        self.screen.blit(pause_text, pause_text_rect)

        # Draw Restart button
        pygame.draw.rect(self.screen, colors['restart'], self.restart_button)
        restart_text = self.font.render("Restart", True, colors['text'])
        restart_text_rect = restart_text.get_rect(center=self.restart_button.center)
        self.screen.blit(restart_text, restart_text_rect)

        # Draw slider
        pygame.draw.rect(self.screen, colors['slider'], self.slider_rect)
        pygame.draw.rect(self.screen, colors['slider_button'], self.slider_button_rect)

        # Add "Slow" and "Fast" labels
        slow_text = self.small_font.render("Slow", True, colors['text'])
        slow_text_rect = slow_text.get_rect(midleft=(self.slider_rect.left, self.slider_rect.bottom + 10))
        self.screen.blit(slow_text, slow_text_rect)

        fast_text = self.small_font.render("Fast", True, colors['text'])
        fast_text_rect = fast_text.get_rect(midright=(self.slider_rect.right, self.slider_rect.bottom + 10))
        self.screen.blit(fast_text, fast_text_rect)

        # Draw Change Style button (adjusted for new width)
        pygame.draw.rect(self.screen, colors['slider'], self.change_style_button)
        style_text = self.font.render("Change Style", True, colors['text'])
        style_text_rect = style_text.get_rect(center=self.change_style_button.center)
        self.screen.blit(style_text, style_text_rect)

    def get_clicked_button(self, pos):
        if self.start_button.collidepoint(pos):
            return "start"
        elif self.pause_button.collidepoint(pos):
            return "pause"
        elif self.restart_button.collidepoint(pos):
            return "restart"
        elif self.slider_rect.collidepoint(pos):
            return "slider"
        elif self.change_style_button.collidepoint(pos):
            return "change_style"
        return None

    def update_slider(self, x):
        x = max(self.slider_rect.left, min(x, self.slider_rect.right - self.slider_button_rect.width))
        self.slider_button_rect.x = x
        return self.get_slider_value()

    def get_slider_value(self):
        slider_range = self.slider_rect.width - self.slider_button_rect.width
        slider_pos = self.slider_button_rect.x - self.slider_rect.x
        # Adjust the calculation to make left slow (0.5) and right fast (0.05)
        return self.slider_max + (self.slider_min - self.slider_max) * (1 - slider_pos / slider_range)
