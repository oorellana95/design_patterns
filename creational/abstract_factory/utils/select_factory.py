from creational.abstract_factory.concrete_products.concrete_product_types_enum import ConcreteProductTypesEnum
from creational.abstract_factory.factories.secure_products_factory import SecureProductsFactory
from creational.abstract_factory.factories.vanilla_products_factory import VanillaProductsFactory


def select_factory(product_type: ConcreteProductTypesEnum):
    factories = {
        ConcreteProductTypesEnum.VANILLA: VanillaProductsFactory,
        ConcreteProductTypesEnum.SECURE: SecureProductsFactory
    }
    factory = factories.get(product_type)

    if not factory:
        raise ValueError(f"Error! Unknown product type: {product_type}")

    return factory()
