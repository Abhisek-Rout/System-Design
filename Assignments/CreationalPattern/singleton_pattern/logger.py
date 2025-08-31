"""
The Logger class implements the Singleton Pattern to provide a single point of access for logging messages throughout the application.
"""
from datetime import datetime

class Logger:
    __instance = None

    def __init__(self):
        if Logger.__instance is not None:
            raise Exception("Use get_instance() instead of direct instantiation")
        Logger.__instance = self

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = Logger()
        return cls.__instance
    
    def __log(self, level: str, message: str):
        dt = datetime.now()
        timestamp: str = dt.strftime("%Y-%m-%d %H:%M:%S.%f")
        print(f"{timestamp} [{level}]: {message}")

    def info(self, message: str):
        self.__log("INFO", message)

    def warn(self, message: str):
        self.__log("WARN", message)

    def error(self, message: str):
        self.__log("ERROR", message)
