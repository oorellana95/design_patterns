from abc import ABC, abstractmethod

from creational.factory_method.transportation_example.transport import Transport, Train, Boat


class Logistics(ABC):
    """
    The Creator class declares the factory method that is supposed to return an
    object of a Product class. The Creator's subclasses usually provide the
    implementation of this method.
    """

    @abstractmethod
    def factory_method(self):
        """
        Note that the Creator may also provide some default implementation of
        the factory method.
        """
        return Transport()

    def some_operation(self) -> str:
        """
        Also note that, despite its name, the Creator's primary responsibility
        is not creating products. Usually, it contains some core business logic
        that relies on Product objects, returned by the factory method.
        Subclasses can indirectly change that business logic by overriding the
        factory method and returning a different type of product from it.
        """

        # Call the factory method to create a Product object.
        transport = self.factory_method()

        # Now, use the product.
        result = f"Creator: The same creator's code has just worked with {transport.deliver()}"

        return result


"""
Concrete Creators override the factory method in order to change the resulting
product's type.
"""


class LandLogistics(Logistics):
    """
    Note that the signature of the method still uses the abstract product type,
    even though the concrete product is actually returned from the method. This
    way the Creator can stay independent of concrete product classes.
    """

    def factory_method(self) -> Transport:
        return Train()


class SeaLogistics(Logistics):
    def factory_method(self) -> Transport:
        return Boat()

