# Metaclass Logger

import logging
import threading

class SingletonMeta(type):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
            return cls._instances[cls]
        
class Logger(metaclass=SingletonMeta):
    _logger = None

    def __init__(self):
        self._initialize_logger()

    def _initialize_logger(self):
         # Set up the logger
        self._logger = logging.getLogger('my_logger')
        self._logger.setLevel(logging.DEBUG)

        # Create a file handler and set its level to DEBUG
        file_handler = logging.FileHandler('my_log_file.log')
        file_handler.setLevel(logging.DEBUG)

        # Create a console handler and set its level to INFO
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Create a formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add the handlers to the logger
        self._logger.addHandler(file_handler)
        self._logger.addHandler(console_handler)

    def getLogger(self):
        return self._logger


if __name__ == "__main__":
    # Testing out the logger
    logger = Logger().getLogger()
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')