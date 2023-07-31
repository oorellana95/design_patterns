from creational.abstract_factory.concrete_products.concrete_product_types_enum import ConcreteProductTypesEnum
from creational.abstract_factory.utils.build_product_components import build_product_components
from creational.abstract_factory.utils.select_factory import select_factory


def main_abstract_factory():
    factory = select_factory(product_type=ConcreteProductTypesEnum.VANILLA)
    build_product_components(factory)
