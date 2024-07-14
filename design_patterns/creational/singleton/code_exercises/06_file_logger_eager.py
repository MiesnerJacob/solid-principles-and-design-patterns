# Filer Writer - Eager Loading Implementation

import datetime

class SingletonMeta(type):
    _instances = {}

    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)
        cls._instances[cls] = super().__call__()

    def __call__(cls, file_name='audit.log'):
        cls._instances[cls]._file_name = file_name
        with open(cls._instances[cls]._file_name, 'a') as file:
            file.write(f"Log started: {datetime.datetime.now()}\n")
        return cls._instances[cls]

class FileAuditManager(metaclass=SingletonMeta):    
    def log_message(self, message):
        timestamp = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")
        with open(self._file_name, 'a') as file:
            file.write(f"{timestamp}: {message}\n")

# Testing the logger
logger = FileAuditManager()
logger.log_message("Test message for eager loading implementation.")