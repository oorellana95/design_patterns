from creational.factory_method.transportation_example.logistics import Logistics, LandLogistics, SeaLogistics


def client_code(logistics: Logistics) -> None:
    """
    The client code works with an instance of a concrete creator, albeit through
    its base interface. As long as the client keeps working with the creator via
    the base interface, you can pass it any creator's subclass.
    """

    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{logistics.some_operation()}", end="")


def main_factory_method_transportation_example():
    client_code(LandLogistics())
    print("\n")
    client_code(SeaLogistics())
