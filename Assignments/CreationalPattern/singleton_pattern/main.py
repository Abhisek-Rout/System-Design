"""
The Exercise class demonstrates how to use the Logger class to log messages of different severity levels. 
"""
from logger import Logger

class Exercise:
    def main(self):
        logger: Logger = Logger.get_instance()

        info_msg: str = input("Enter an info msg: ")
        logger.info(info_msg)

        warn_msg: str = input("Enter an warn msg: ")
        logger.warn(warn_msg)

        error_msg: str = input("Enter an error msg: ")
        logger.info(error_msg)

if __name__ == "__main__":
    obj: Exercise = Exercise()
    obj.main()