import copy


class Singleton:
    value = []

    def __new__(cls):
        """In the source code, I override the classes __new__ method to return a reference to itself.
        This then makes the __init__ method irrelevant.
        commenting out the __new__ method, and you will see that the IDs of the instances no longer point to the same
        memory location of the class, but to new memory identifiers instead."""
        return cls

    # def __init__(self):
    #     print("in init")

    @staticmethod
    def static_method():
        """Use @staticmethod if no inner variables required"""

    @classmethod
    def class_method(cls):
        """Use @classmethod to access class level variables"""
        print(cls.value)


def main_singleton_concept():
    # All uses of singleton point to the same memory address (id)
    print(f"id(Singleton)\t= {id(Singleton)}")

    OBJECT1 = Singleton()
    print(f"id(OBJECT1)\t= {id(OBJECT1)}")

    OBJECT2 = copy.deepcopy(OBJECT1)
    print(f"id(OBJECT2)\t= {id(OBJECT2)}")

    OBJECT3 = Singleton()
    print(f"id(OBJECT1)\t= {id(OBJECT3)}")
