from creational.abstract_factory.abstract_products.messenger import Messenger


class VanillaMessenger(Messenger):
    """
    Type: Concrete Product
    Abstract methods of the Messenger base class are implemented.
    """

    # Interface - Create Messenger Window
    def create_messenger_window(self):
        print("Messenger Window Created")