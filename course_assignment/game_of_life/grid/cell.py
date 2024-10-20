# Uses State Design Pattern
from abc import ABC, abstractmethod

class CellState(ABC):
    @abstractmethod
    def next_state(self, live_neighbors):
        pass

class AliveState(CellState):
    def next_state(self, live_neighbors):
        if live_neighbors < 2 or live_neighbors > 3:
            return DeadState()
        return self

class DeadState(CellState):
    def next_state(self, live_neighbors):
        if live_neighbors == 3:
            return AliveState()
        return self

class Cell:
    def __init__(self, state=DeadState()):
        self._state = state

    def is_alive(self):
        return isinstance(self._state, AliveState)

    def next_state(self, live_neighbors):
        return Cell(self._state.next_state(live_neighbors))
