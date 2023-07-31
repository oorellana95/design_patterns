from abc import ABCMeta, abstractmethod


class IHouseBuilder(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def set_building_type(building_type):
        pass

    @staticmethod
    @abstractmethod
    def set_wall_material(wall_material):
        pass

    @staticmethod
    @abstractmethod
    def set_number_doors(number):
        pass

    @staticmethod
    @abstractmethod
    def set_number_windows(number):
        pass

    @staticmethod
    @abstractmethod
    def get_result():
        pass