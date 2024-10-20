import pygame
import numpy as np
from game_of_life.grid.grid import Grid
from game_of_life.grid.cell import Cell

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Grid dimensions
n_cells_x, n_cells_y = 40, 30
cell_width = width // n_cells_x
cell_height = height // n_cells_y

# Initialize the grid
cells = [[Cell(np.random.choice([True, False], p=[0.2, 0.8])) for _ in range(n_cells_x)] for _ in range(n_cells_y)]
grid = Grid(cells)

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)
green = (0, 255, 0)

# Button dimensions
button_width, button_height = 200, 50
button_x, button_y = (width - button_width) // 2, height - button_height - 10

def draw_button():
    pygame.draw.rect(screen, green, (button_x, button_y, button_width, button_height))
    font = pygame.font.Font(None, 36)
    text = font.render("Next Generation", True, black)
    text_rect = text.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))
    screen.blit(text, text_rect)

def draw_grid():
    for y in range(0, height, cell_height):
        for x in range(0, width, cell_width):
            cell = pygame.Rect(x, y, cell_width, cell_height)
            pygame.draw.rect(screen, gray, cell, 1)

def draw_cells():
    for y in range(n_cells_y):
        for x in range(n_cells_x):
            cell = pygame.Rect(x * cell_width, y * cell_height, cell_width, cell_height)
            if grid.cells[y][x].is_alive():
                pygame.draw.rect(screen, black, cell)

running = True
while running:
    screen.fill(white)
    draw_grid()
    draw_cells()
    draw_button()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_x <= event.pos[0] <= button_x + button_width and button_y <= event.pos[1] <= button_y + button_height:
                grid.update()
            else:
                x, y = event.pos[0] // cell_width, event.pos[1] // cell_height
                grid.cells[y][x].update(not grid.cells[y][x].is_alive())

pygame.quit()
