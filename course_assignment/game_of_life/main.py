# Uses all Design Patterns from the course

import pygame
from game.game import Game
from game.game_state import RunningState
from game.game_ticker import GameTicker
from grid.grid_builder import GridBuilder
from grid.cell_factory import RandomCellFactory
from renderer.classic_renderer import ClassicRenderer
from input_adapter.input_adapter import InputAdapter
from renderer.dark_mode_renderer import DarkModeRenderer

def main():
    # Screen dimensions
    width, height = 800, 600

    # Grid dimensions
    n_cells_x, n_cells_y = 40, 28  # Reduced y to leave space for buttons
    cell_width = width // n_cells_x
    cell_height = (height - 70) // n_cells_y  # Subtract 70 for button space

    # Create Singleton Game instance
    game = Game()
    game.initialize(width, height, cell_width, cell_height)

    # Set Game State
    game.set_state(RunningState(game))

    # Build Grid using Builder and Factory Method
    cell_factory = RandomCellFactory()
    grid_builder = (GridBuilder()
                    .set_size(n_cells_y, n_cells_x)
                    .set_cell_factory(cell_factory)
                    .set_alive_probability(0.2))
    game.set_grid_builder(grid_builder)
    game.grid = grid_builder.build()

    # Set Renderer (Strategy Pattern)
    renderer = ClassicRenderer(width, height, cell_width, cell_height)
    game.renderer = renderer

    # Set GameTicker with initial speed
    initial_speed = 0.2  # A moderate initial speed
    ticker = GameTicker(interval=initial_speed)
    game.ticker = ticker

    # Set initial slider position in renderer
    initial_slider_pos = renderer.slider_rect.left + (
        (initial_speed - renderer.slider_max) / (renderer.slider_min - renderer.slider_max)
    ) * (renderer.slider_rect.width - renderer.slider_button_rect.width)
    renderer.update_slider(initial_slider_pos)
    game.set_speed(initial_speed)  # Ensure the game speed is set initially

    # Set InputAdapter (Adapter Pattern)
    input_adapter = InputAdapter(game)

    # Main game loop
    clock = pygame.time.Clock()
    running = True
    while running:
        running = input_adapter.process_input()
        game.update()
        game.render()
        clock.tick(60)  # Limit to 60 FPS

    pygame.quit()

if __name__ == "__main__":
    main()
