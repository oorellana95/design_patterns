from creational.abstract_factory.factories.abstract_factory import AbstractFactory
from creational.abstract_factory.concrete_products.vanilla import VanillaBrowser, VanillaMessenger


class VanillaProductsFactory(AbstractFactory):
    """
    Type: Concrete Factory
    Implement the operations to create concrete product objects.
    """

    def create_browser(self):
        return VanillaBrowser()

    def create_messenger(self):
        return VanillaMessenger()

