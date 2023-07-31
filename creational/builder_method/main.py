from creational.builder_method.house.directors import IglooDirector, CastleDirector, HouseBoatDirector


def main_builder_method():
    IGLOO = IglooDirector.construct()
    CASTLE = CastleDirector.construct()
    HOUSEBOAT = HouseBoatDirector.construct()

    print(IGLOO.construction())
    print(CASTLE.construction())
    print(HOUSEBOAT.construction())
