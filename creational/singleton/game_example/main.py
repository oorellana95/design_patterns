from creational.singleton.game_example.games.game1 import Game1
from creational.singleton.game_example.games.game2 import Game2
from creational.singleton.game_example.games.game3 import Game3


def main_singleton_game_example():
    game_1 = Game1()
    game_1.add_winner(2, "Cosmo")

    game_2 = Game2()
    game_2.add_winner(3, "Sean")

    game_3 = Game3()
    game_3.add_winner(1, "Emmy")

    game_1.leaderboard.print()
    game_2.leaderboard.print()
    game_3.leaderboard.print()
