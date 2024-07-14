# Simple Singleton Logger

import logging
import threading

class SingletonLogger:
    _instance = None
    _lock = threading.Lock()

    @classmethod
    def get_instance(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = cls()
                cls._instance._initialize_logger()
            return cls._instance
        
    def _initialize_logger(self):
        # Set up the logger
        self.logger = logging.getLogger('my_logger')
        self.logger.setLevel(logging.DEBUG)

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
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

# Testing out the logger
logger = SingletonLogger().get_instance().logger
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')