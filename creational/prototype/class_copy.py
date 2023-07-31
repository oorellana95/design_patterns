import copy
from creational.prototype.prototype import IProtoType


class ClassCopy(IProtoType):
    def __init__(self, field):
        self.field = field

    def clone(self, mode):
        modes = {
            1: self.field,  # results in a 1 level shallow copy of the Document
            2: self.field.copy(),  # results in a 2 level shallow copy of the Document
            3: copy.deepcopy(self.field)  # recursive deep copy. Slower but results in a new copy where no
            # sub elements are shared by reference
        }

        field = modes.get(mode)
        if field:
            return type(self)(
                field
            )

        raise ValueError(f"Error! Unknown mode: {mode}")

    def __str__(self):
        return f"{id(self)}\tfield={self.field}\ttype={type(self.field)}"
