# Uses Builder Design Pattern
from grid.cell_factory import RandomCellFactory
from grid.grid import Grid

class GridBuilder:
    def __init__(self):
        self.rows = 30
        self.cols = 30
        self.cell_factory = RandomCellFactory()
        self.alive_prob = 0.2

    def set_size(self, rows, cols):
        self.rows = rows
        self.cols = cols
        return self

    def set_cell_factory(self, cell_factory):
        self.cell_factory = cell_factory
        return self

    def set_alive_probability(self, prob):
        self.alive_prob = prob
        return self

    def build(self):
        cells = [
            [self.cell_factory.create_cell(self.alive_prob) for _ in range(self.cols)]
            for _ in range(self.rows)
        ]
        return Grid(cells)
