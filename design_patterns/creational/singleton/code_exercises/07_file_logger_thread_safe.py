# Filer Writer - Thread Safe Eager Loading Implementation

import threading
import datetime

class FileAuditManager:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, file_name='audit.log'):
        with cls._lock:
            cls._instance = super(FileAuditManager, cls).__new__(cls)
            cls._instance._file_name = file_name
            with open(cls._instance._file_name, 'a') as file:
                file.write(f"Log started: {datetime.datetime.now()}\n")
            return cls._instance
        
    def log_message(cls, message):
        with cls._lock:
            timestamp = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")
            with open(cls._instance._file_name, 'a') as file:
                file.write(f"{timestamp}: {message}\n")

# Testing the logger
def write_to_logs():
    logger = FileAuditManager()
    logger.log_message("Test message for thread-safe metaclass eager loading implementation.")

threads = []

for i in range(10):
    t = threading.Thread(target=write_to_logs)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()