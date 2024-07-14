# Filer Writer - Lazy Loading Implementation

import datetime

class FileAuditManager:
    _instance = None

    def __new__(cls, file_name='audit.log'):
        if cls._instance is None:
            cls._instance = super(FileAuditManager, cls).__new__(cls)
            cls._instance._file_name = file_name
            with open(cls._instance._file_name, 'a') as file:
                file.write(f"Log started: {datetime.datetime.now()}\n")
        return cls._instance
        
    def log_message(self, message):
        timestamp = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")
        with open(self._file_name, 'a') as file:
            file.write(f"{timestamp}: {message}\n")

# Testing the logger
logger = FileAuditManager()
logger.log_message("Test message for lazy loading implementation.")