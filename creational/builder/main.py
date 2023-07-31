from creational.builder.house.directors.castle_director import CastleDirector
from creational.builder.house.directors.houseboat_director import HouseBoatDirector
from creational.builder.house.directors.igloo_director import IglooDirector


def main_builder():
    IGLOO = IglooDirector.construct()
    CASTLE = CastleDirector.construct()
    HOUSEBOAT = HouseBoatDirector.construct()

    print(IGLOO.construction())
    print(CASTLE.construction())
    print(HOUSEBOAT.construction())
