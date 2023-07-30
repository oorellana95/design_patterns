from creational.abstract_factory_method.concrete_products.ConcreteProductTypesEnum import ConcreteProductTypesEnum
from creational.abstract_factory_method.factories.SecureProductsFactory import SecureProductsFactory
from creational.abstract_factory_method.factories.VanillaProductsFactory import VanillaProductsFactory


def select_factory(product_type: ConcreteProductTypesEnum):
    factories = {
        ConcreteProductTypesEnum.VANILLA: VanillaProductsFactory,
        ConcreteProductTypesEnum.SECURE: SecureProductsFactory
    }
    factory = factories.get(product_type)

    if not factory:
        raise ValueError(f"Error! Unknown product type: {product_type}")

    return factory()
