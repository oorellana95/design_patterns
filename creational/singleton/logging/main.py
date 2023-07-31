from creational.singleton.logging.logger import Logger
from creational.singleton.logging.logger_not_singleton import LoggerNotSingleton


def main_logging_example():
    logger_1 = Logger()
    print(f"ID Logger Singleton 1: {id(logger_1)}")
    logger_1.error("Fail", "CE0102")

    logger_2 = Logger()
    print(f"ID Logger Singleton 2: {id(logger_2)}")
    logger_2.warning("Warning", "CW0008")

    logger_3 = LoggerNotSingleton()
    print(f"ID Logger Not Singleton 3: {id(logger_3)}")
    logger_3.error("Fail", "CI001")

    logger_4 = LoggerNotSingleton()
    print(f"ID Logger Not Singleton 4: {id(logger_4)}")
    logger_4.warning("Warning", "CI002")

    # Note: It is not required to initialize Logger()
    Logger.warning("Warning", "2000")



