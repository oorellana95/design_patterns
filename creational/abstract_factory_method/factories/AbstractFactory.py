from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    """
    The Abstract Factory
    """

    @abstractmethod
    def create_browser(self):
        pass

    @abstractmethod
    def create_messenger(self):
        pass