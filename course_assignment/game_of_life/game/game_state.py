# Uses State Design Pattern
from abc import ABC, abstractmethod

class GameState(ABC):
    def start(self):
        pass

    def pause(self):
        pass

    def stop(self):
        pass

class RunningState(GameState):
    def __init__(self, game):
        self.game = game

    def pause(self):
        print("Pausing game...")
        self.game.set_state(PausedState(self.game))
        self.game.ticker.stop()

class PausedState(GameState):
    def __init__(self, game):
        self.game = game

    def start(self):
        print("Resuming game...")
        self.game.set_state(RunningState(self.game))
        self.game.ticker.start()
