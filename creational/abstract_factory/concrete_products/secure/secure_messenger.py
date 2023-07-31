from creational.abstract_factory.abstract_products.messenger import Messenger


class SecureMessenger(Messenger):
    """
    Type: Concrete Product
    Abstract methods of the Messenger base class are implemented.
    """

    # Abstract Method of the Messenger base class
    def create_messenger_window(self):
        print("Secure Messenger - Messenger Window Created")

    def create_privacy_filter(self):
        print("Secure Messenger - Privacy Filter Created")

    def disappearing_messages(self):
        print("Secure Messenger - Disappearing Messages Feature Enabled")