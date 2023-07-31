from abc import ABC, abstractmethod


class IProtoType(ABC):
    @abstractmethod
    def clone(self, mode):
        """The clone, deep or shallow.
        It is up to you how you want to implement
        the details in your concrete class"""
