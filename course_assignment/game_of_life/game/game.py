# Uses Singleton Design Pattern, State Design Pattern, Observer Design Pattern
from renderer.renderer_style import RendererStyle
from renderer.classic_renderer import ClassicRenderer
from renderer.neon_renderer import NeonRenderer
from renderer.dark_mode_renderer import DarkModeRenderer
import time

class Game:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Game, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.state = None
        self.grid = None
        self.renderer = None
        self.ticker = None
        self.is_running = False
        self.grid_builder = None
        self.width = None
        self.height = None
        self.cell_width = None
        self.cell_height = None
        self.renderer_styles = list(RendererStyle)
        self.current_style_index = 0
        self.renderer_factory = {
            RendererStyle.CLASSIC: ClassicRenderer,
            RendererStyle.NEON: NeonRenderer,
            RendererStyle.DARK: DarkModeRenderer
        }
        self.last_update_time = time.time()

    def initialize(self, width, height, cell_width, cell_height):
        self.width = width
        self.height = height
        self.cell_width = cell_width
        self.cell_height = cell_height

    def set_state(self, state):
        self.state = state

    def set_grid_builder(self, grid_builder):
        self.grid_builder = grid_builder

    def start(self):
        if not self.is_running:
            self.is_running = True
            self.state.start()
            self.last_update_time = time.time()

    def pause(self):
        if self.is_running:
            self.is_running = False
            self.state.pause()

    def restart(self):
        self.is_running = False
        self.grid = self.grid_builder.build()
        self.state.pause()

    def update(self):
        current_time = time.time()
        if self.is_running and current_time - self.last_update_time >= self.ticker.interval:
            self.grid.update()
            self.last_update_time = current_time

    def render(self):
        if self.renderer and self.grid:
            self.renderer.render(self.grid, self.is_running)

    def set_speed(self, speed):
        if self.ticker:
            # Ensure the speed is within the correct range
            clamped_speed = max(self.renderer.slider_max, min(self.renderer.slider_min, speed))
            self.ticker.set_interval(clamped_speed)

    def change_style(self):
        self.current_style_index = (self.current_style_index + 1) % len(self.renderer_styles)
        new_style = self.renderer_styles[self.current_style_index]
        renderer_class = self.renderer_factory[new_style]
        self.renderer = renderer_class(self.width, self.height, self.cell_width, self.cell_height)
        print(f"Changed style to: {new_style.name}")  # Debug print
