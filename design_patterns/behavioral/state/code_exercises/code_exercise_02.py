from abc import ABC, abstractmethod

class PlayerState(ABC):

    @abstractmethod
    def play(self, player):
        pass

    @abstractmethod
    def stop(self, player):
        pass

    @abstractmethod
    def pause(self, player):
        pass

class StoppedState(PlayerState):
    def play(self, player):
        print("Starting playback...")
        player.state = PlayingState()

    def stop(self, player):
        print("Player is already stopped.")

    def pause(self, player):
        print("Player is already paused.")

class PlayingState(PlayerState):
    def play(self, player):
        print("Player is already playing.")

    def stop(self, player):
        print("Stopping playback...")
        player.state = StoppedState()
    
    def pause(self, player):
        print("Pausing playback...")
        player.state = PausedState()

class PausedState(PlayerState):
    def play(self, player):
        print("Resuming playback...")
        player.state = PlayingState()

    def stop(self, player):
        print("Stopping playback...")
        player.state = StoppedState()

    def pause(self, player):
        print("Player is already paused.")


class Player:
    def __init__(self):
        self.state = StoppedState()

    def play(self):
        self.state.play(self)

    def stop(self):
        self.state.stop(self)

    def pause(self):
        self.state.pause(self)


def main():
    player = Player()
    player.play()
    player.pause()
    player.stop()

    player.stop()
    player.pause()

if __name__ == "__main__":
    main()