from creational.builder.house.directors import IglooDirector, CastleDirector, HouseBoatDirector


if __name__ == "__main__":
    IGLOO = IglooDirector.construct()
    CASTLE = CastleDirector.construct()
    HOUSEBOAT = HouseBoatDirector.construct()

    print(IGLOO.construction())
    print(CASTLE.construction())
    print(HOUSEBOAT.construction())
