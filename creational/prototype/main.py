from creational.prototype.class_copy import ClassCopy


def execute_copy(mode, object_0):
    object_1 = ClassCopy(object_0)
    print(f"\nMode: {mode}")
    print(f"OBJECT_1 {object_1}")
    object_2 = object_1.clone(mode)  # Clone
    object_2.field[1] = 101
    object_2.field[4][2] = 100
    print(f"OBJECT_2 {object_2}")
    print(f"OBJECT_1 {object_1}")


def main_prototype():
    object_0 = [1, 2, 3, 4, [1, 2, 3]]
    execute_copy(mode=1, object_0=object_0)
    object_0 = [1, 2, 3, 4, [1, 2, 3]]
    execute_copy(mode=2, object_0=object_0)
    object_0 = [1, 2, 3, 4, [1, 2, 3]]
    execute_copy(mode=3, object_0=object_0)
