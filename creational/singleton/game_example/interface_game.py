from abc import ABC, abstractmethod


class IGame(ABC):
    @staticmethod
    @abstractmethod
    def add_winner(position, name):
        pass
