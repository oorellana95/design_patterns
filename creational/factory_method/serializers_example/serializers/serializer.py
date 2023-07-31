from abc import ABC, abstractmethod


class Serializer(ABC):
    @abstractmethod
    def start_object(self, object_name, object_id):
        pass

    def add_property(self, name, value) -> str:
        pass

    def to_str(self) -> str:
        pass
