# Uses Factory Design Pattern
import numpy as np
from grid.cell import AliveState, DeadState, Cell

class CellFactory:
    def create_cell(self, alive_prob):
        raise NotImplementedError()

class RandomCellFactory(CellFactory):
    def create_cell(self, alive_prob):
        state = AliveState() if np.random.random() < alive_prob else DeadState()
        return Cell(state)
