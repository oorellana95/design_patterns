from abc import ABC, abstractmethod


class Messenger(ABC):
    """
    Creates "Abstract Product B"
    """

    @abstractmethod
    # Interface - Create Messenger Window
    def create_messenger_window(self):
        pass
