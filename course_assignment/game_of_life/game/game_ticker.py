# Uses Observer Design Pattern
import threading
import time
from threading import Thread, Event

class GameTicker:
    def __init__(self, interval=0.5):
        self.interval = interval
        self.last_update = time.time()
        self._stop_event = Event()
        self._thread = None

    def start(self):
        if self._thread is None or not self._thread.is_alive():
            self._stop_event.clear()
            self._thread = Thread(target=self._run)
            self._thread.start()

    def stop(self):
        self._stop_event.set()
        if self._thread:
            self._thread.join()

    def _run(self):
        while not self._stop_event.is_set():
            current_time = time.time()
            if current_time - self.last_update >= self.interval:
                self.last_update = current_time
                # Notify observers or update game state here
            time.sleep(0.01)  # Small sleep to prevent busy-waiting

    def set_interval(self, interval):
        self.interval = max(0.05, min(0.5, interval))  # Clamp between 0.05 and 0.5

    def should_update(self):
        current_time = time.time()
        if current_time - self.last_update >= self.interval:
            self.last_update = current_time
            return True
        return False
