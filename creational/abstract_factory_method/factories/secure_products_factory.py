from creational.abstract_factory_method.factories.abstract_factory import AbstractFactory
from creational.abstract_factory_method.concrete_products.secure import SecureBrowser, SecureMessenger


class SecureProductsFactory(AbstractFactory):
    """
    Type: Concrete Factory
    Implement the operations to create concrete product objects.
    """

    def create_browser(self):
        return SecureBrowser()

    def create_messenger(self):
        return SecureMessenger()
