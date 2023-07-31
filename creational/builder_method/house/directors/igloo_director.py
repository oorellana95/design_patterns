from creational.builder_method.house.house_builder import HouseBuilder


class IglooDirector:
    @staticmethod
    def construct():
        """
        Note that in this IglooDirector, it has omitted the set_number_of
        windows call since this Igloo will have no windows.
        """
        return HouseBuilder()\
            .set_building_type("Igloo")\
            .set_wall_material("Ice")\
            .set_number_doors(1)\
            .get_result()
