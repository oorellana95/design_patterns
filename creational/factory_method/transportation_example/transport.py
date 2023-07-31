from abc import ABC, abstractmethod


class Transport(ABC):
    """
    The Product interface declares the operations that all concrete products
    must implement.
    """

    @abstractmethod
    def deliver(self) -> str:
        pass


"""
Concrete Products provide various implementations of the Product interface.
"""


class Train(Transport):
    def deliver(self) -> str:
        return "{Result of the Train}"


class Boat(Transport):
    def deliver(self) -> str:
        return "{Result of the Boat}"
