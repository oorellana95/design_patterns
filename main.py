from creational.abstract_factory.main import main_abstract_factory
from creational.builder.main import main_builder
from creational.factory_method.serializers_example.main import main_factory_method_serializers_example
from creational.factory_method.transportation_example.main import main_factory_method_transportation_example
from creational.prototype.main import main_prototype
from creational.singleton.game_example.main import main_singleton_game_example
from creational.singleton.logging.main import main_logging_example
from creational.singleton.main_singleton_concept import main_singleton_concept
from structural.adapter.car_example.main import main_adapter_car_example
from structural.adapter.conceptual.main import main_adapter


def execute_creational_design_patterns():
    main_abstract_factory()
    main_builder()
    main_factory_method_serializers_example()
    main_factory_method_transportation_example()
    main_prototype()
    main_singleton_concept()
    main_singleton_game_example()
    main_logging_example()


def execute_structural_design_patterns():
    main_adapter_car_example()
    #main_adapter()


if __name__ == '__main__':
    execute_structural_design_patterns()
