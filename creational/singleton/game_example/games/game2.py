from creational.singleton.game_example.interface_game import IGame
from creational.singleton.game_example.leaderboard import Leaderboard


class Game2(IGame):
    def __init__(self):
        self.leaderboard = Leaderboard()

    def add_winner(self, position, name):
        self.leaderboard.add_winner(position, name)